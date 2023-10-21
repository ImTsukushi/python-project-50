from gendiff.file_parsing import absolute_path, get_format, parsing_file


def stylish_diff(file_path1: str, file_path2: str) -> str:
    abs_path1 = absolute_path(file_path1)
    abs_path2 = absolute_path(file_path2)
    file_format1 = get_format(file_path1)
    file_format2 = get_format(file_path2)
    data1 = parsing_file(abs_path1, file_format1)
    data2 = parsing_file(abs_path2, file_format2)

    keys = sorted(set(data1.keys()) | set(data2.keys()))
    diff = []

    for key in keys:
        if key in data1 and key in data2:
            if data1[key] == data2[key]:
                diff.append(f'  {key}: {data1[key]}')
            else:
                diff.append(f'- {key}: {data1[key]}')
                diff.append(f'+ {key}: {data2[key]}')
        elif key in data1:
            diff.append(f'- {key}: {data1[key]}')
        else:
            diff.append(f'+ {key}: {data2[key]}')
    return '{\n' + '\n'.join(diff) + '\n}'
