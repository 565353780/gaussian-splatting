from gaussian_splatting.Method.render import renderTrainGS

def demo():
    output_folder_path = '../gaussian-splatting/output/PolyTech_fine/'
    port = 6006

    renderTrainGS(output_folder_path, port)
    return True
