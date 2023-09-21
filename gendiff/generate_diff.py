from gendiff.utils import parsing


def generate_diff(path1, path2):
    file1 = parsing.get_file_contents(path1)
    file2 = parsing.get_file_contents(path2)

    diff = get_diff(file1, file2)

    return diff


def make_new_diff_entry(key, new_value, old_value=None, state='unchanged'):
    return {
        'key': key,
        'new_value': new_value,
        'old_value': old_value,
        'state': state,
        'children': get_diff(old_value, new_value)
    }


def get_diff(file1, file2):
    deleted_keys = set(file1.keys()) - set(file2.keys())
    added_keys = set(file2.keys()) - set(file1.keys())
    common_keys = set(file1.keys()).intersection(set(file2.keys()))
    changed_keys = {
        key for key in common_keys if file1[key] != file2[key]
    }

    diff = []

    for key in sorted(set(file1.keys()) | set(file2.keys())):
        value1 = file1[key]
        value2 = file2[key]
        if key in deleted_keys:
            diff.append(make_new_diff_entry(key, None, value1, state='deleted'))
        elif key in added_keys:
            diff.append(make_new_diff_entry(key, value2, state='added'))
        elif key in changed_keys:
            diff.append(make_new_diff_entry(key, value2, value1, state='changed'))
        elif isinstance(value1, dict) and isinstance(value2, dict):
            diff.append(make_new_diff_entry(key, value2, value1, state='nested'))
        else:
            diff.append(make_new_diff_entry(key, value1, state='unchanged'))

    return diff