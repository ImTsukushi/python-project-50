def plain_value(value):
    """
    Функция изменяет значения под json формат
    """
    if isinstance(value, dict):
        return '[complex value]'
    elif isinstance(value, bool):
        return str(value).lower()
    elif value is None:
        return 'null'
    elif isinstance(value, int):
        return value
    return f"'{value}'"


def branch_changed(value, current_path):
    return (f"Property '{current_path}' was updated. "
            f"From {plain_value(value['old'])} to {plain_value(value['new'])}")


def branch_removed(value, current_path):
    return f"Property '{current_path}' was removed"


def branch_added(value, current_path):
    return (f"Property '{current_path}' was added "
            f"with value: {plain_value(value['value'])}")


def plain_format(diff_result: dict) -> str:
    """
    Функция рекурсивно преобразует разницу в файлах
    в строковую форму в формате plain text
    """
    operations = {
        'changed':
            branch_changed,
        'removed':
            branch_removed,
        'added':
            branch_added,
        'nested':
            lambda value, current_path: walk(value['value'], current_path + '.')
    }

    def walk(node, path):
        result = []
        for key, value in node.items():
            current_path = f"{path}{value['key']}"
            operation = value['operation']
            if operation in operations:
                result.append(operations[operation](value, current_path))
        return '\n'.join(result)

    return walk(diff_result, '')
