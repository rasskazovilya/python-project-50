def format_diff_stylish(diff):
    text = format_diff(diff)
    return '{\n' + text + '}'


def format_diff(diff, tab=1):
    text = ''
    for entry in diff:
        key = entry['key']
        if entry['state'] == 'added':
            text += format_line(key, entry["new_value"], '+', tab)
        elif entry['state'] == 'deleted':
            text += format_line(key, entry["old_value"], '-', tab)
        elif entry['state'] == 'changed':
            text += format_line(key, entry["old_value"], '-', tab)
            text += format_line(key, entry["new_value"], '+', tab)
        elif entry['state'] == 'unchanged':
            text += format_line(key, entry["new_value"], ' ', tab)
        elif entry['state'] == 'nested':
            text += ' ' * 4 * tab + '{\n'
            text += format_diff(entry['children'], tab+1)
            text += ' ' * 4 * tab + '}\n'
    return text


def format_line(key, value, op, tab):
    indent = ' ' * (4 * tab - 2)
    return f'{indent}{op} {key}: {value}\n'
