import sys

sys.path.append("../camera-manage/")

from gaussian_splatting.Method.render import renderTrainGS
from gaussian_splatting.Method.time import getLatestFolderName

data_folder_name_dict = {
    "0": "NeRF/3vjia_simple",
    "1": "NeRF/wine",
    "2": "NeRF/cup_1",
    "3": "UrbanScene3D/PolyTech_fine_zhang",
}

data_folder_name = data_folder_name_dict["2"].replace("/", "_")
data_folder_name = getLatestFolderName(
    data_folder_name, "../gaussian-splatting/output/"
)

output_folder_path = "../gaussian-splatting/output/" + data_folder_name + "/"
port = 6007

renderTrainGS(output_folder_path, port)
