from gendiff.utils import parsing


def generate_diff(path1, path2):
    file1 = parsing.get_file_contents(path1)
    file2 = parsing.get_file_contents(path2)

    deleted_keys = set(file1.keys()) - set(file2.keys())
    added_keys = set(file2.keys()) - set(file1.keys())
    common_keys = set(file1.keys()).intersection(set(file2.keys()))
    changed_keys = {
        key for key in common_keys if file1[key] != file2[key]
        }
    unchanged_keys = {
        key for key in common_keys if file1[key] == file2[key]
        }

    diff = '{\n'
    for key in sorted(set(file1.keys()) | set(file2.keys())):
        if key in deleted_keys:
            diff += f'  - {key}: {file1[key]}\n'
        if key in added_keys:
            diff += f'  + {key}: {file2[key]}\n'
        if key in unchanged_keys:
            diff += f'    {key}: {file1[key]}\n'
        if key in changed_keys:
            diff += f'  - {key}: {file1[key]}\n'
            diff += f'  + {key}: {file2[key]}\n'
    diff += '}'

    return diff
