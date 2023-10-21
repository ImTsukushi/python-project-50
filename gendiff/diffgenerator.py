from gendiff.formats.stylish import stylish_diff
from gendiff.file_parsing import parsing_file


def generate_diff(file_path1: str, file_path2: str, style="stylish") -> str:
    if style == "stylish":
        data = stylish_diff(file_path1, file_path2)
        return data
