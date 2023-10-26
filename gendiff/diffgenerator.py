from gendiff.formats.stylish import stylish_format
from gendiff.formats.plain import plain_format
from gendiff.makediff import build_diff


def generate_diff(file_path1: str, file_path2: str, style="stylish") -> str:
    if style == "stylish":
        data = stylish_format(build_diff(file_path1, file_path2))
        return data
    elif style == "plain":
        data = plain_format(build_diff(file_path1, file_path2))
        return data
