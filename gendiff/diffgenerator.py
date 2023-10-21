from gendiff.formats.stylish import stylish_diff


def generate_diff(file_path1: str, file_path2: str, style="stylish") -> str:
    if style == "stylish":
        data = stylish_diff(file_path1, file_path2)
        return data
