import yaml 
import os


def read_yaml(config_path: str) -> dict:
    with open(config_path) as yaml_file:
        config = yaml.safe_load(yaml_file)
    return config
