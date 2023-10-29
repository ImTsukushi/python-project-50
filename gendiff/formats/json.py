import json


def json_child(value):
    """
    Функция рекурсивно форматирует вложенные словари
    """
    if isinstance(value, dict):
        return {k: json_child(v) for k, v in value.items()}
    return None if value == '' else value


def json_format(diff_result):
    """
    Функция форматирует разницу двух файлов в формат json
    """
    result = json_child(diff_result)
    return json.dumps(result)
