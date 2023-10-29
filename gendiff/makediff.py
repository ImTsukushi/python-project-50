from gendiff.file_parsing import absolute_path, get_format, parsing_file


def compare_dicts(dict1: dict, dict2: dict) -> dict:
    """
    Функция принимает файлы в виде словарей и возвращает
    разницу между ними в виде словарей
    """
    keys = sorted(dict1.keys() | dict2.keys())
    result = {}
    for key in keys:
        if key in dict1 and key in dict2:
            if dict1[key] == dict2[key]:
                description = \
                    {'key': key, 'operation': 'unchanged', 'value': dict1[key]}
            elif isinstance(dict1[key], dict) and isinstance(dict2[key], dict):
                description = \
                    {'key': key, 'operation': 'nested', 'value':
                        compare_dicts(dict1[key], dict2[key])}
            else:
                description = \
                    {'key': key, 'operation': 'changed', 'old':
                        dict1[key], 'new': dict2[key]}
        elif key in dict1:
            description = \
                {'key': key, 'operation': 'removed', 'value': dict1[key]}
        else:
            description = \
                {'key': key, 'operation': 'added', 'value': dict2[key]}
        result[key] = description
    return result


def build_diff(file_path1: str, file_path2: str) -> dict:
    """
    Функция принимает пути до файлов и возвращает разницу
    между ними в виде словаря
    """
    abs_paths = map(absolute_path, [file_path1, file_path2])
    file_formats = map(get_format, [file_path1, file_path2])
    dicts = map(parsing_file, abs_paths, file_formats)
    dict1, dict2 = dicts
    result = compare_dicts(dict1, dict2)
    return result
