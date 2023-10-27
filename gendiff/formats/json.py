import json


def json_value(value):
    if isinstance(value, dict):
        return {k: json_value(v) for k, v in value.items()}
    return None if value == '' else value


def json_format(diff_result):
    result = json_value(diff_result)
    return json.dumps(result)
