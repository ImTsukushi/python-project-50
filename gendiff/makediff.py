from gendiff.file_parsing import absolute_path, get_format, parsing_file


def build_diff(file_path1, file_path2):
    abs_path1, abs_path2 = map(absolute_path, [file_path1, file_path2])
    file_format1, file_format2 = map(get_format, [file_path1, file_path2])
    dict1, dict2 = map(parsing_file, [abs_path1, abs_path2], [file_format1, file_format2])

    def same_or_different(dict1, dict2):
        keys = dict1.keys()
        return keys & dict2.keys(), keys - dict2.keys(), dict2.keys() - keys

    def diff(dict1, dict2):
        keys = sorted(dict1.keys() | dict2.keys())
        same, removed, added = same_or_different(dict1, dict2)
        result = {}
        for key in keys:
            if key in removed:
                description = {'key': key, 'operation': 'removed', 'value': dict1[key]}
            elif key in added:
                description = {'key': key, 'operation': 'added', 'value': dict2[key]}
            elif key in same:
                if dict1[key] == dict2[key]:
                    description = {'key': key, 'operation': 'unchanged', 'value': dict1[key]}
                elif isinstance(dict1[key], dict) and isinstance(dict2[key], dict):
                    description = {'key': key, 'operation': 'nested', 'value': diff(dict1[key], dict2[key])}
                else:
                    description = {'key': key, 'operation': 'changed', 'old': dict1[key], 'new': dict2[key]}
            result[key] = description
        return result

    return diff(dict1, dict2)


if __name__ == "__main__":
    file_path1 = "/home/nexus/hexlet-projects/python-project-50/tests/fixtures/trees/nestedfile1.json"
    file_path2 = "/home/nexus/hexlet-projects/python-project-50/tests/fixtures/trees/nestedfile2.json"
    diff = build_diff(file_path1, file_path2)
    print(diff)
