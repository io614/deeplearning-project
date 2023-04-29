import os
import glob
import re
import json
import pandas as pd

def get_config_dicts(results_folder = "results/permute/"):
    """
    Returns list of dictionaries containing properties of each configuration, including paths to the results.json files
    """
    
    d_results_glob = "*d_results.json"
    z_results_glob = "*z_results.json"

    config_folders = sorted(os.listdir(results_folder))

    itemss = [tuple([folder] + re.split('_', folder)) for folder in config_folders]
    keys =  ("folder", "base_model", "scoring_model", "mask_model", "sampling")

    config_dicts = [{key:item for key, item in zip(keys, items)} for items in itemss]

    def get_d_path(folder_name):
        # sort by date and return the latest d path
        return sorted(glob.glob(f"{results_folder}{folder_name}/**/{d_results_glob}"))[-1]
        
    def get_z_path(folder_name):
        # sort by date and return the latest z path
        return sorted(glob.glob(f"{results_folder}{folder_name}/**/{z_results_glob}"))[-1]

    config_dicts = [{**config_dict, "d_path": get_d_path(config_dict["folder"]), "z_path": get_z_path(config_dict["folder"])} for config_dict in config_dicts]

    return config_dicts

def get_pred_df(base_model, drop_scoring_base=False, pred_type="z", shuffle=False):
    """
    For a given base model, return a DataFrame containing d/z scores from different scoring models, and y-label (0=real, 1=sampled)
    """

    path="d_path" if (pred_type=="d") else "z_path"

    config_dicts=get_config_dicts()
    config_dicts_base = [config_dict for config_dict in config_dicts if config_dict["base_model"]==base_model]

    results_dicts = [{"scoring_model": d["scoring_model"],"path": d[path], } for d in config_dicts_base]

    def get_xy_from_json(results_json_path):

        with open(results_json_path, "r") as f:
            data = json.load(f)

        real_preds = data['predictions']['real']
        sample_preds = data['predictions']['samples']

        assert len(real_preds) == len(sample_preds)

        x = real_preds + sample_preds
        y = [0] * len(real_preds) + [1] * len(sample_preds)

        assert len(x) == len(y)
        return dict(x=x, y=y)

    results_dicts = [{**d, **get_xy_from_json(d["path"])} for d in results_dicts]
    x_dict = {d['scoring_model']:d['x'] for d in results_dicts}
    df = pd.DataFrame(x_dict)
    df["y"] = results_dicts[0]["y"]

    if drop_scoring_base:
        df = df.drop(base_model, axis=1)

    if shuffle:
        df = df.sample(frac=1).reset_index(drop=True)
        
    return df