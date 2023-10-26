import sys

sys.path.append("../camera-manage/")

from gaussian_splatting.Method.render import renderTrainGS

data_folder_name = "NeRF/cup_1"

output_folder_path = (
    "../gaussian-splatting/output/" + data_folder_name.replace("/", "_") + "/"
)
port = 6006

renderTrainGS(output_folder_path, port)
