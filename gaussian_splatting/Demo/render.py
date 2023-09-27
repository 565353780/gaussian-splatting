from gaussian_splatting.Method.render import renderTrainGS

def demo():
    output_folder_path = '../gaussian-splatting/output/3vjia_simple/'
    port = 6006

    renderTrainGS(output_folder_path, port)
    return True
