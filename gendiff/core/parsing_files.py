import json
import yaml
from pathlib import Path


def get_file_content(file_path):
    file_path = Path(file_path)
    extension = file_path.suffix[1:]

    with open(file_path) as file:
        if extension == 'json':
            return json.load(file)
        elif extension in ('yml', 'yaml'):
            return yaml.safe_load(file)
        else:
            raise ValueError(f"Unsupported file format: {extension}")


def get_parse_file(file_path):
    return get_file_content(file_path)
