import sys

sys.path.append("../camera-manage/")

from gaussian_splatting.Method.render import renderTrainGS

data_folder_name = "NeRF/wine"
data_folder_name = "NeRF/3vjia_simple"

output_folder_path = (
    "../gaussian-splatting/output/" + data_folder_name.replace("/", "_") + "/"
)
port = 6007

renderTrainGS(output_folder_path, port)
