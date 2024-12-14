import json
import yaml


def get_parse_file(file_path):
    extension = file_path.split('.')[-1]
    if extension == 'json':
        with open(file_path, 'r') as file:
            return json.load(file)
    elif extension in ('yml', 'yaml'):
        with open(file_path, 'r') as file:
            return yaml.safe_load(file)
