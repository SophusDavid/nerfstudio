from pathlib import Path


root = Path("./")
raw_data = root / "raw_data"
data_fold = root / "data"

import subprocess

for dataset in data_fold.iterdir():
    setname = dataset.stem
    if setname !='4' :
        continue
    config_path=root/'outputs'/setname/'nerfacto'/'Final'/'config.yml'
    camera_paths_path=dataset/'camera_paths'
    for cam_path in camera_paths_path.iterdir():
        path_idx=cam_path.stem
        output_path=root/'renders'/setname/(path_idx+'.mp4')
        
        process = subprocess.Popen(
            [
                "ns-render",
                "--load-config",
                str(config_path),
               "--traj","filename",
                "--camera-path-filename",
                str(cam_path),
                "--output-path",
                str(output_path)
            ]
        )
        process.wait()
    # process = subprocess.Popen(
    #     [
    #         "ns-train",
    #         "nerfacto",
    #         "--data",
    #         str(data_fold / setname),
    #         "--pipeline.model.predict-normals",
    #         "True",
    #         "--viewer.quit-on-train-completion",
    #         "True",
    #     ]
    # )
    # process.wait()


# ns-render --load-config outputs/1/nerfacto/2023-03-18_114025/config.yml --traj filename --camera-path-filename data/1/camera_paths/2023-03-18_114025.json --output-path renders/1/2023-03-18_114025.mp4
