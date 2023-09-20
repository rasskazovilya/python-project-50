import json
import yaml
from pathlib import Path


def get_file_contents(path):
    loaders = {
        '.json': json.load,
        '.yml': yaml.safe_load,
        '.yaml': yaml.safe_load
    }
    path = Path(path)
    with open(path) as file:
        file_suffix = path.suffix
        return loaders[file_suffix](file)
