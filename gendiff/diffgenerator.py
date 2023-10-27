from gendiff.formats.stylish import stylish_format
from gendiff.formats.plain import plain_format
from gendiff.formats.json import json_format
from gendiff.makediff import build_diff

FORMATS = {
    "stylish": stylish_format,
    "plain": plain_format,
    "json": json_format,
}


def generate_diff(file_path1: str, file_path2: str, style="stylish") -> str:
    format_func = FORMATS.get(style)
    if format_func:
        data = format_func(build_diff(file_path1, file_path2))
        return data
