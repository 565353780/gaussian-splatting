import sys
sys.path.append('../colmap-manage/')

from colmap_manage.Module.colmap_manager import COLMAPManager
from colmap_manage.Module.dataset_manager import DatasetManager

data_folder_path = '/home/chli/chLi/Dataset/NeRF/3vjia_simple/'
remove_old = False
valid_percentage = 0.8
dataset_folder_path = '../colmap-manage/output/3vjia_simple/'

COLMAPManager(data_folder_path).autoGenerateData(remove_old, valid_percentage)
DatasetManager().autoGenerateDataset(data_folder_path, dataset_folder_path)