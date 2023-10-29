import yaml
import json
import os
from pathlib import PurePosixPath


def absolute_path(path: str) -> str:
    """
    Функция принимает путь до файла и
    возвращает абсолютный путь до него
    """
    return os.path.abspath(path)


def get_format(path: str) -> str:
    """
    Функция принимает путь до файла и
    возвращает его формат
    """
    return PurePosixPath(path).suffix[1:]


def parsing_file(path: str, file_format: str) -> dict:
    """
    Функция принимает путь до файла и его формат.
    Возвращает содержимое файла адаптированное
    для питона
    """
    with open(path, 'r', encoding='utf-8') as file:
        if file_format == 'json':
            return json.load(file)
        elif file_format == 'yaml' or file_format == 'yml':
            return yaml.safe_load(file)
