from gendiff.formats.stylish import format_diff_stylish
from gendiff.formats.plain import format_diff_plain
from gendiff.formats.json import format_diff_json


def format_diff(diff, format='stylish'):
    formatters = {
        'stylish': format_diff_stylish,
        'plain': format_diff_plain,
        'json': format_diff_json
    }
    return formatters[format](diff)