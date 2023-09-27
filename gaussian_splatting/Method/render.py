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
