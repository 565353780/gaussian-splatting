from gaussian_splatting.Method.render import renderTrainGS

def demo():
    output_folder_path = '../colmap-manage/output/3vjia_simple/gs/'
    port = 6006

    renderTrainGS(output_folder_path, port)
    return True
