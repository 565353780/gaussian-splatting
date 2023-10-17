import sys
sys.path.append('../camera-manage/')

from gaussian_splatting.Method.render import renderTrainGS

output_folder_path = '../gaussian-splatting/output/NeRF_usb/'
port = 6006

renderTrainGS(output_folder_path, port)
