TRAIN_CONFIG = {
    "dataset_folder_path": "../colmap-manage/output/<folder-name>/gs/",
    "output_folder_path": "../gaussian-splatting/output/<folder-name>/",
    "start_checkpoint": None,
    "iterations": 40000,
    "resolution": 8,
    "ip": "127.0.0.1",
    "port": 6007,
    "device": "cuda",
    "percent_dense": 0.01,
    "detect_anomaly": False,
    "test_iterations": [7000, 30000, 40000],
    "save_iterations": [7000, 30000, 40000],
    "checkpoint_iterations": [],
    "quiet": False,
}


def getTrainConfig(folder_name):
    train_config = TRAIN_CONFIG
    train_config["dataset_folder_path"] = train_config["dataset_folder_path"].replace(
        "<folder-name>", folder_name
    )
    train_config["output_folder_path"] = train_config["output_folder_path"].replace(
        "<folder-name>", folder_name
    )
    return train_config
