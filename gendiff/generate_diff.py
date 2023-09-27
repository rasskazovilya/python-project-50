from gendiff.formats.choose_format import format_diff
from gendiff.utils import parsing, read_file


def generate_diff(path1, path2, format='stylish'):
    data1, data_format1 = read_file.get_contents_suffix(path1)
    data2, data_format2 = read_file.get_contents_suffix(path2)
    parsed_data1 = parsing.parse(data1, data_format1)
    parsed_data2 = parsing.parse(data2, data_format2)
    diff = get_diff(parsed_data1, parsed_data2)
    return format_diff(diff, format)


def make_new_diff_entry(key, new_value, old_value):
    entry = {
        'key': key,
        'new_value': new_value,
        'old_value': old_value,
    }
    state = 'unchanged'
    if old_value == '_empty':
        state = 'added'
    elif new_value == '_empty':
        state = 'deleted'
    elif isinstance(new_value, dict) and isinstance(old_value, dict):
        state = 'nested'
        entry.update({'children': get_diff(old_value, new_value)})
    elif new_value != old_value:
        state = 'changed'
    entry.update({'state': state})
    return entry


def get_diff(serial_data1, serial_data2):
    diff = []
    for key in sorted(set(serial_data1.keys()) | set(serial_data2.keys())):
        value1 = serial_data1.get(key, '_empty')
        value2 = serial_data2.get(key, '_empty')
        diff.append(make_new_diff_entry(key, value2, value1))
    return diff
