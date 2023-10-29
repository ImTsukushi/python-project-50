import itertools


def stylish_value(value, depth):
    """
    Функция изменяет значения под json формат
    """
    if isinstance(value, dict):
        string = ''
        for key, value in value.items():
            space = '    ' * (depth + 1)
            string += f"\n{space}{key}: {stylish_value(value, depth + 1)}"
        s = itertools.chain('{', string, '\n', ['    ' * depth, '}'])
        return ''.join(s)
    else:
        if isinstance(value, bool):
            return str(value).lower()
        elif value is None:
            return 'null'
        else:
            return str(value)


def build_string(dictionary, key, depth, sign='  '):
    """
    Преобразует значения в строку
    """
    string = f"{'  ' * depth}{sign}{dictionary['key']}: " \
             f"{stylish_value(dictionary[key], depth + 1)}"
    return string


def stylish_format(diff_result: dict) -> str:
    """
    Функция рекурсивно преобразует разницу в файлах
    в строковую форму в формате stylish text
    """
    def walk(node, depth, replacer='  '):
        space = replacer * (depth + 1)
        strings = ''
        operation_mapping = {
            'nested': lambda v, depth, space:
            f"\n{space * 2}{v['key']}: {walk(v['value'], depth + 1)}",
            'unchanged': lambda v, depth, space:
            f"\n{space}{build_string(v, 'value', depth)}",
            'changed': lambda v, depth, space:
            f"\n{space}{build_string(v, 'old', depth, '- ')}\n{space}"
            f"{build_string(v, 'new', depth, '+ ')}",
            'removed': lambda v, depth, space:
            f"\n{space}{build_string(v, 'value', depth, '- ')}",
            'added': lambda v, depth, space:
            f"\n{space}{build_string(v, 'value', depth, '+ ')}",
        }

        for key, value in node.items():
            if value['operation'] in operation_mapping:
                strings += (operation_mapping[value['operation']]
                            (value, depth, space))

        result = itertools.chain('{', strings, '\n', ['    ' * depth + '}'])
        return ''.join(result)

    return walk(diff_result, 0)
