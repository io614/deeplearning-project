import os
import glob
import re

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