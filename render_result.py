import sys

sys.path.append("../camera-manage/")

from gaussian_splatting.Method.render import renderGSResult
from gaussian_splatting.Method.time import getLatestFolderName

nerf_list = ['chair', 'hotdog', 'mic', 'ship']
nerf = nerf_list[1]
data_folder_name_dict = {
    "0": "NeRF/3vjia_simple",
    "1": "NeRF/wine",
    "2": "NeRF/cup_1",
    "3": "UrbanScene3D/PolyTech_fine_zhang",
    "4": "NeRF/oven-train",
    "5": "NeRF/real_fridge-train",
    "6": "NeRF/real_fridge_raw-train",
    "7": "NeRF/" + nerf + "_train",
}

data_folder_name = data_folder_name_dict["7"].replace("/", "_")
data_folder_name = getLatestFolderName(
    data_folder_name, "../gaussian-splatting/output/"
)

output_folder_path = "../gaussian-splatting/output/" + data_folder_name + "/"
iteration = None

renderGSResult(output_folder_path, iteration)
