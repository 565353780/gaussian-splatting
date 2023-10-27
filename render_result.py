import sys

sys.path.append("../camera-manage/")

from gaussian_splatting.Method.render import renderGSResult

output_folder_path = "../gaussian-splatting/output/UrbanScene3D_PolyTech_fine_zhang/"
output_folder_path = "../gaussian-splatting/output/NeRF_wine/"
iteration = None

renderGSResult(output_folder_path, iteration)
