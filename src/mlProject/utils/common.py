# YAML files read + Helper utilities
import os
from box.exceptions import BoxValueError
import yaml
from mlProject import logger
import json
import joblib
from ensure import ensure_annotations
from box import ConfigBox
from pathlib import Path


# Reads a YAML file from `path_to_yaml`, logs success, and returns the parsed content
# wrapped in a ConfigBox (dot-notation access). Raises ValueError if YAML is empty.
@ensure_annotations
def read_yaml(path_to_yaml: Path) -> ConfigBox:
    try:
        with open(path_to_yaml, encoding="utf-8") as yaml_file:
            content = yaml.safe_load(yaml_file)
            logger.info(f"yaml file: {path_to_yaml} Loaded successfully")
            return ConfigBox(content)
    except BoxValueError:
        raise ValueError("yaml file is empty")
    except Exception as e:
        raise e

@ensure_annotations # Creates Directories
def create_directories(path_to_directories: list, verbose: bool = True):
    for path in path_to_directories:
        os.makedirs(path, exist_ok=True)
        if verbose:
            logger.info(f"created directory at: {path}")

@ensure_annotations
def save_json(path: object, data: dict) -> None:
    path = Path(path)
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4)
    logger.info(f"json file saved at: {path}")

@ensure_annotations
def load_json(path: Path) -> ConfigBox:
    with open(path, encoding="utf-8") as f:
        content = json.load(f)

    logger.info(f"JSON file successfully loaded from: {path}")
    return ConfigBox(content)

@ensure_annotations
def save_bin(data: object, path: Path):
    joblib.dump(value=data, filename=path)
    logger.info(f"Binary file saved at {path}")

@ensure_annotations
def load_bin(path: Path) -> object:
    data = joblib.load(path)
    logger.info(f"Binary file loaded from {path}")
    return data

@ensure_annotations
def get_size(path: object) -> str:
    path = Path(path)
    size_in_kb = round(os.path.getsize(path) / 1024)
    return f"~ {size_in_kb} KB"