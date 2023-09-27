import json
import yaml


def parse(data, format):
    loaders = {
        'json': json.loads,
        'yml': yaml.safe_load,
        'yaml': yaml.safe_load
    }
    return loaders[format](data)
