from gaussian_splatting.Method.train import trainGS

def demo():
    dataset_folder_path = '../colmap-manage/output/3vjia_simple/gs/'
    output_folder_path = '../gaussian_splatting/output/test0/'
    image_folder_name = 'images'
    resolution = 1
    device = 'cuda'
    iterations = 30000
    port = 6006
    percentent_dense = 0.01

    trainGS(dataset_folder_path, output_folder_path, image_folder_name,
            resolution, device, iterations, port, percentent_dense)
    return True
