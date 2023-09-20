from gendiff.utils import parsing


def generate_diff(path1, path2):
    first_file = parsing.get_file_contents(path1)
    second_file = parsing.get_file_contents(path2)

    deleted_keys = set(first_file.keys()) - set(second_file.keys())
    added_keys = set(second_file.keys()) - set(first_file.keys())
    common_keys = set(first_file.keys()).intersection(set(second_file.keys()))
    changed_keys = {
        key for key in common_keys if first_file[key] != second_file[key]
        }
    unchanged_keys = {
        key for key in common_keys if first_file[key] == second_file[key]
        }

    diff = '{\n'
    for key in sorted(set(first_file.keys()) | set(second_file.keys())):
        if key in deleted_keys:
            diff += f'  - {key}: {first_file[key]}\n'
        if key in added_keys:
            diff += f'  + {key}: {second_file[key]}\n'
        if key in unchanged_keys:
            diff += f'    {key}: {first_file[key]}\n'
        if key in changed_keys:
            diff += f'  - {key}: {first_file[key]}\n'
            diff += f'  + {key}: {second_file[key]}\n'
    diff += '}'

    return diff
