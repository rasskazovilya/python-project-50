from gendiff.utils import parsing
from gendiff.formats.choose_format import format_diff


def generate_diff(path1, path2, format= 'stylish'):
    file1 = parsing.get_file_contents(path1)
    file2 = parsing.get_file_contents(path2)

    diff = get_diff(file1, file2)
    
    return format_diff(diff, format)


def make_new_diff_entry(key, new_value, old_value):
    entry = {
        'key': key,
        'new_value': new_value,
        'old_value': old_value,
    }

    if old_value is None:
        state = 'added'
    elif new_value is None:
        state = 'deleted'
    elif isinstance(new_value, dict) and isinstance(old_value, dict):
        state = 'nested'
        entry.update({'children': get_diff(old_value, new_value)})
    elif new_value != old_value:
        state = 'changed'
    else:
        state = 'unchanged'
    entry.update({'state': state})

    return entry


def get_diff(file1, file2):
    diff = []

    for key in sorted(set(file1.keys()) | set(file2.keys())):
        value1 = file1.get(key, None)
        value2 = file2.get(key, None)
        diff.append(make_new_diff_entry(key, value2, value1))

    return diff
