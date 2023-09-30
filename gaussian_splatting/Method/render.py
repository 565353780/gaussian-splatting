import os
from gaussian_splatting.Method.cmd import runCMD

def renderTrainGS(output_folder_path, port=6006):
    if not os.path.exists(output_folder_path):
        print('[ERROR][render::renderTrainGS]')
        print('\t output_folder not exist!')
        print('\t output_folder_path:', output_folder_path)
        return False

    cmd = '../gs/SIBR_viewers/install/bin/SIBR_remoteGaussian_app' + \
        ' --port ' + str(port) + \
        ' --path ' + output_folder_path

    if not runCMD(cmd, True):
        print('[ERROR][render::renderTrainGS]')
        print('\t runCMD failed!')
        print('\t cmd:', cmd)
        return False

    return True

def renderGSResult(output_folder_path, iteration=None):
    if not os.path.exists(output_folder_path):
        print('[ERROR][render::renderGSResult]')
        print('\t output_folder not exist!')
        print('\t output_folder_path:', output_folder_path)
        return False

    iteration_root_folder_path = output_folder_path + 'point_cloud/'
    if not os.path.exists(iteration_root_folder_path):
        print('[ERROR][render::renderGSResult]')
        print('\t iteration_root_folder not exist! please train and wait!')
        print('\t iteration_root_folder_path:', iteration_root_folder_path)
        return False

    if iteration is None:
        iteration_idx_list = []

        iteration_folder_name_list = os.listdir(iteration_root_folder_path)

        for iteration_folder_name in iteration_folder_name_list:
            if iteration_folder_name[:10] != 'iteration_':
                continue

            iteration_idx_list.append(int(iteration_folder_name[10:]))

        if len(iteration_idx_list) == 0:
            print('[ERROR][render::renderGSResult]')
            print('\t iteration_folder not found! please train and wait!')
            print('\t iteration_root_folder_path:', iteration_root_folder_path)
            return False

        iteration_idx_list.sort()

        iteration_folder_path = iteration_root_folder_path + 'iteration_' + str(iteration_idx_list[-1]) + '/'
    else:
        iteration_folder_path = output_folder_path + 'point_cloud/iteration_' + str(iteration)

    if not os.path.exists(iteration_folder_path):
        print('[ERROR][render::renderGSResult]')
        print('\t iteration_folder not exist!')
        print('\t iteration_folder_path:', iteration_folder_path)
        return False

    print('[INFO][render::renderGSResult]')
    print('\t start render result...')
    print('\t data loaded from:', iteration_folder_path)

    cmd = '../gs/SIBR_viewers/install/bin/SIBR_gaussianViewer_app' + \
	    ' --model-path ' + output_folder_path + \
        ' --iteration ' + str(iteration)

    if not runCMD(cmd, True):
        print('[ERROR][render::renderGSResult]')
        print('\t runCMD failed!')
        print('\t cmd:', cmd)
        return False

    return True
