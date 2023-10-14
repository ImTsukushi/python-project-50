import json
import os

def stylish_diff(file_path1: str, file_path2: str) -> str:
    file_path1 = os.path.abspath(file_path1)
    file_path2 = os.path.abspath(file_path2)
    with open(file_path1, 'r') as file1, open(file_path2, 'r') as file2:
        data1 = json.load(file1)
        data2 = json.load(file2)
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
