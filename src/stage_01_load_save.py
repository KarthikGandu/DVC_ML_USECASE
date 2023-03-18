from utils.all_utils import read_yaml
import argparse
import os
import pandas as pd


def get_data(config_path):
    config = read_yaml(config_path)
    #print(config)
    df = pd.read_csv(config["data_source"], sep=";")
    #print(df.head())
    artifcats_dir = config["artifacts"]["artifacts_dir"]
    raw_local_dir = config["artifacts"]["raw_local_dir"]
    raw_local_file = config["artifacts"]["raw_local_file"]
    raw_local_dir_path = os.path.join(artifcats_dir, raw_local_dir)
    create_directory(dirs=[raw_local_dir_path])
    
    raw_local_file_path = os.path.join(raw_local_dir_path, raw_local_file)
    
    df.to_csv(raw_local_file_path, sep=",", index=False)
    #print(df.head())



def create_directory(dirs: list):
    for dir_path in dirs:
        os.makedirs(dir_path, exist_ok=True)
        print(f"created directory: {dir_path}")


if __name__ == "__main__":
    args = argparse.ArgumentParser()
    args.add_argument("--config", "-c", default="config/config.yaml")
    parsed_args = args.parse_args()
    config = read_yaml(parsed_args.config)
    #print(config)
    get_data(config_path=parsed_args.config)
    #df = pd.read_csv(config["data_source"])
    #print(df.head())

