import sys

sys.path.append("../camera-manage/")

from gaussian_splatting.Method.render import renderTrainGS
from gaussian_splatting.Method.time import getLatestFolderName

nerf_list = ['chair', 'hotdog', 'mic', 'ship']
nerf = nerf_list[3]
data_folder_name_dict = {
    "0": "NeRF/3vjia_simple",
    "1": "NeRF/wine",
    "2": "NeRF/cup_1",
    "3": "UrbanScene3D/PolyTech_fine_zhang",
    "4": "NeRF/jfguo-virtual-1-images",
    "5": "NeRF/jfguo-real-1-images",
    "6": "NeRF/real_fridge_raw-train",
    "7": "NeRF/" + nerf + "_train",
}

data_folder_name = data_folder_name_dict["7"].replace("/", "_")
data_folder_name = getLatestFolderName(
    data_folder_name, "../gaussian-splatting/output/"
)

output_folder_path = "../gaussian-splatting/output/" + data_folder_name + "/"
port = 6007

renderTrainGS(output_folder_path, port)
