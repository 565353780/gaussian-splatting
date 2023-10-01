import os
import torch
from random import randint

from gaussian_splatting.Config.params import ModelParams, PipelineParams, OptimizationParams
from gaussian_splatting.Config.train import TRAIN_CONFIG
from gaussian_splatting.Loss.loss import l1_loss, ssim
from gaussian_splatting.Method.model import safe_state
from gaussian_splatting.Model.gaussians import GaussianModel
from gaussian_splatting.Data.scene import Scene
from gaussian_splatting.Method.render import render
from gaussian_splatting.Method.train import prepare_output_and_logger, training_report

class Controller(object):
    def __init__(self):
        self.source_path = TRAIN_CONFIG['dataset_folder_path']
        self.model_path = TRAIN_CONFIG['output_folder_path']
        self.iterations = TRAIN_CONFIG['iterations']
        self.resolution = TRAIN_CONFIG['resolution']
        self.percent_dense = TRAIN_CONFIG['percent_dense']

        self.detect_anomaly = TRAIN_CONFIG['detect_anomaly']
        self.test_iterations = TRAIN_CONFIG['test_iterations']
        self.save_iterations = TRAIN_CONFIG['save_iterations']
        self.checkpoint_iterations = TRAIN_CONFIG['checkpoint_iterations']
        self.quiet = TRAIN_CONFIG['quiet']
        self.start_checkpoint = TRAIN_CONFIG['start_checkpoint']

        # Params
        self.lp = ModelParams()
        self.lp.source_path = self.source_path
        self.lp.model_path = self.model_path
        self.lp.resolution = self.resolution

        self.op = OptimizationParams()
        self.op.percent_dense = self.percent_dense

        self.pp = PipelineParams()

        # Model
        self.gaussians = GaussianModel(self.lp.sh_degree)
        self.first_iter = 0
        self.scene = Scene(self.lp, self.gaussians)
        self.gaussians.training_setup(self.op)

        # Log
        self.tb_writer = prepare_output_and_logger(self.lp)

        # Render
        bg_color = [1, 1, 1] if self.lp.white_background else [0, 0, 0]
        self.background = torch.tensor(bg_color, dtype=torch.float32, device="cuda")

        # Initialize system state (RNG)
        safe_state(self.quiet)

        # Start GUI server, configure and run training
        torch.autograd.set_detect_anomaly(self.detect_anomaly)
        return

    def loadModel(self, model_file_path):
        if not os.path.exists(model_file_path):
            print('[ERROR][Trainer::loadModel]')
            print('\t model file not exist!')
            print('\t model_file_path:', model_file_path)
            return False

        (model_params, self.first_iter) = torch.load(self.start_checkpoint)
        self.gaussians.restore(model_params, self.op)
        return True

    def saveModel(self, ply_file_path):
        self.gaussians.save_ply(ply_file_path)
        return True

    def trainStep(self, viewpoint_cam):
        # Render
        render_pkg = render(viewpoint_cam, self.gaussians, self.pp, self.background)
        image = render_pkg["render"]

        # Loss
        gt_image = viewpoint_cam.original_image.cuda()
        Ll1 = l1_loss(image, gt_image)
        loss = (1.0 - self.op.lambda_dssim) * Ll1 + self.op.lambda_dssim * (1.0 - ssim(image, gt_image))
        loss.backward()
        return Ll1, loss, render_pkg

    def train(self):
        if self.start_checkpoint:
            self.loadModel(self.start_checkpoint)

        viewpoint_stack = None
        ema_loss_for_log = 0.0

        self.first_iter += 1
        for iteration in range(self.first_iter, self.op.iterations + 1):
            self.gaussians.update_learning_rate(iteration)

            # Every 1000 its we increase the levels of SH up to a maximum degree
            if iteration % 1000 == 0:
                self.gaussians.oneupSHdegree()

            # Pick a random Camera
            if not viewpoint_stack:
                viewpoint_stack = self.scene.getTrainCameras().copy()
            viewpoint_cam = viewpoint_stack.pop(randint(0, len(viewpoint_stack)-1))

            Ll1, loss, render_pkg = self.trainStep(viewpoint_cam)

            viewspace_point_tensor, visibility_filter, radii = render_pkg["viewspace_points"], render_pkg["visibility_filter"], render_pkg["radii"]

            with torch.no_grad():
                # Progress bar
                ema_loss_for_log = 0.4 * loss.item() + 0.6 * ema_loss_for_log

                # Log and save
                training_report(self.tb_writer, iteration, Ll1, loss, l1_loss, None, self.test_iterations, self.scene, render, (self.pp, self.background))

                # Densification
                if iteration < self.op.densify_until_iter:
                    # Keep track of max radii in image-space for pruning
                    self.gaussians.max_radii2D[visibility_filter] = torch.max(self.gaussians.max_radii2D[visibility_filter], radii[visibility_filter])
                    self.gaussians.add_densification_stats(viewspace_point_tensor, visibility_filter)

                    if iteration > self.op.densify_from_iter and iteration % self.op.densification_interval == 0:
                        size_threshold = 20 if iteration > self.op.opacity_reset_interval else None
                        self.gaussians.densify_and_prune(self.op.densify_grad_threshold, 0.005, self.scene.cameras_extent, size_threshold)
                    
                    if iteration % self.op.opacity_reset_interval == 0 or (self.lp.white_background and iteration == self.op.densify_from_iter):
                        self.gaussians.reset_opacity()

                # Optimizer step
                if iteration < self.op.iterations:
                    self.gaussians.optimizer.step()
                    self.gaussians.optimizer.zero_grad(set_to_none = True)

                if (iteration in self.checkpoint_iterations):
                    print("\n[ITER {}] Saving Checkpoint".format(iteration))
                    torch.save((self.gaussians.capture(), iteration), self.scene.model_path + "/chkpnt" + str(iteration) + ".pth")
        return True
