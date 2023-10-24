from gendiff.makediff import build_diff
import itertools


def stylish_value(value, depth):
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
    string = f"{'  ' * depth}{sign}{dictionary['key']}: " \
             f"{stylish_value(dictionary[key], depth + 1)}"
    return string


def stylish_format(diff_result):

    def walk(node, depth, replacer='  '):
        space = replacer * (depth + 1)
        strings = ''
        for k, v in node.items():
            if v['operation'] == 'nested':
                strings += f"\n{space * 2}{v['key']}: {walk(v['value'], depth + 1)}"
            elif v['operation'] == 'unchanged':
                strings += f"\n{space}{build_string(v, 'value', depth)}"
            elif v['operation'] == 'changed':
                strings += f"\n{space}{build_string(v, 'old', depth, '- ')}"
                strings += f"\n{space}{build_string(v, 'new', depth, '+ ')}"
            elif v['operation'] == 'removed':
                strings += f"\n{space}{build_string(v, 'value', depth, '- ')}"
            elif v['operation'] == 'added':
                strings += f"\n{space}{build_string(v, 'value', depth, '+ ')}"
        result = itertools.chain('{', strings, '\n', ['    ' * depth + '}'])
        return ''.join(result)
    return walk(diff_result, 0)


if __name__ == "__main__":
    file_path1 = "/home/nexus/hexlet-projects/python-project-50/tests/fixtures/trees/file1.json"
    file_path2 = "/home/nexus/hexlet-projects/python-project-50/tests/fixtures/trees/file2.json"
    diff = build_diff(file_path1, file_path2)
    buuuu = stylish_format(diff)
    print(buuuu)
