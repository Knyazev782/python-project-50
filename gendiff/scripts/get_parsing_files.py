import json
import yaml

def parse_file(file_path):
    if file_path.endswith(('.yml', '.yaml')):
        with open(file_path, 'r') as file:
            return yaml.safe_load(file)
    elif file_path.endswith('.json'):
        with open(file_path, 'r') as file:
            return json.load(file)
