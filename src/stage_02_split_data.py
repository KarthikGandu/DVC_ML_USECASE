from utils.all_utils import read_yaml
import argparse
import os
import pandas as pd
from sklearn.model_selection import train_test_split


'''def get_data(config_path):
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

    #splittting the data
    train, test = train_test_split(df, test_size=0.3, random_state=42)
    
    #df.to_csv(raw_local_file_path, sep=",", index=False)
    #print(df.head())'''

def split_data(config_path, params_path):
    config = read_yaml(config_path)
    params = read_yaml(params_path)
    #print(config)
    df = pd.read_csv(config["data_source"], sep=";")
    #print(df.head())
    artifcats_dir = config["artifacts"]["artifacts_dir"]
    raw_local_dir = config["artifacts"]["raw_local_dir"]
    raw_local_file = config["artifacts"]["raw_local_file"]
    raw_local_dir_path = os.path.join(artifcats_dir, raw_local_dir)
    create_directory(dirs=[raw_local_dir_path])
    raw_local_file_path = os.path.join(raw_local_dir_path, raw_local_file)
    split_ratio = params["base"]["test_size"]
    random_state = params["base"]["random_state"]

    #splittting the data
    train, test = train_test_split(df, test_size=split_ratio, random_state=random_state)

    # saving the data train and test
    split_data_dir = config["artifacts"]["split_data_dir"]
    create_directory(dirs=[os.path.join(artifcats_dir, split_data_dir)])
    train_data_filename = config["artifacts"]["train"]
    test_data_filename = config["artifacts"]["test"]

    train_data_path = os.path.join(artifcats_dir, split_data_dir, train_data_filename)
    test_data_path = os.path.join(artifcats_dir, split_data_dir, test_data_filename)

    for data, data_path in (train, train_data_path), (test, test_data_path):
        save_local_df(data, data_path)

    

   
def save_local_df(df, file_name):
    df.to_csv(file_name, sep=",", index=False)
    print(f"saved file at: {file_name} ")


def create_directory(dirs: list):
    for dir_path in dirs:
        os.makedirs(dir_path, exist_ok=True)
        print(f"created directory: {dir_path}")


if __name__ == "__main__":
    args = argparse.ArgumentParser()
    args.add_argument("--config", "-c", default="config/config.yaml")
    args.add_argument("--params", "-p", default="params.yaml")
    parsed_args = args.parse_args()
    config = read_yaml(parsed_args.config)
    #print(config)
    split_data(config_path=parsed_args.config, params_path=parsed_args.params)
    #df = pd.read_csv(config["data_source"])
    #print(df.head())

