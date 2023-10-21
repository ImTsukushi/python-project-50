import yaml
import json
import os
from pathlib import PurePosixPath


def absolute_path(path):
    return os.path.abspath(path)


def get_format(file):
    return PurePosixPath(file).suffix[1:]


def read_file(path):
    with open(path, 'r', encoding='utf-8') as file:
        return file.read()


def parsing_file(path, file_format):
    if file_format == 'json':
        with open(path, 'r', encoding='utf-8') as file:
            return json.load(file)
    elif file_format == 'yaml' or file_format == 'yml':
        with open(path, 'r', encoding='utf-8') as file:
            return yaml.safe_load(file)
