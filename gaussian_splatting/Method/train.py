import os
from gaussian_splatting.Method.cmd import runCMD

def trainGS(dataset_folder_path,
            output_folder_path='../gaussian_splatting/output/test0/',
            image_folder_name='images', resolution=1, device='cuda', iterations=30000,
            port=6006, percentent_dense=0.01):
    if os.path.exists(output_folder_path):
        cmd = 'rm -rf ' + output_folder_path

        if not runCMD(cmd, True):
            print('[ERROR][train::trainGS]')
            print('\t runCMD failed!')
            print('\t cmd:', cmd)
            return False

    cmd = 'cd ../gs && python train.py' + \
        ' --source_path ' + dataset_folder_path + \
        ' --model_path ' + output_folder_path + \
        ' --images ' + image_folder_name + \
        ' --resolution ' + str(resolution) + \
        ' --data_device ' + device + \
        ' --iterations ' + str(iterations) + \
        ' --port ' + str(port) + \
        ' --percent_dense ' + str(percentent_dense)

    if not runCMD(cmd, True):
        print('[ERROR][train::trainGS]')
        print('\t runCMD failed!')
        print('\t cmd:', cmd)
        return False

    return True
