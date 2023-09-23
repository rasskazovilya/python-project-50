def format_diff_stylish(diff):
    text = ''.join(map(format_entry, diff))
    return '{\n' + text + '}'


def format_entry(entry, tab=1):
    key = entry.get('key')
    old = entry.get('old_value')
    new = entry.get('new_value')
    children = entry.get('children')
    state = entry['state']

    operations = {
        'added': lambda _, value: format_line(key, value, '+', tab),
        'deleted': lambda value, _: format_line(key, value, '-', tab),
        'changed': lambda old, new: format_changed(key, old, new, tab),
        'unchanged': lambda value, _: format_line(key, value, ' ', tab),
        'nested': lambda children, _: format_line(key, children, ' ', tab),
    }

    if state == 'nested':
        return operations[state](children, None)
    return operations[state](old, new)


def format_changed(key, old, new, tab):
    return format_line(key, old, '-', tab) + format_line(key, new, '+', tab)


def format_line(key, value, op, tab):
    indent = ' ' * (4 * tab - 2)
    text = format_value(value, tab)
    return f'{indent}{op} {key}: {text}\n'


def format_value(value, tab):
    result = value
    if isinstance(value, bool):
        result = str(value).lower()
    elif value is None:
        result = 'null'
    elif isinstance(value, dict):
        lines = [format_line(k, v, ' ', tab + 1) for k, v in value.items()]
        result = format_multiline(lines, tab)
    elif isinstance(value, list):
        lines = [format_entry(v, tab + 1) for v in value]
        result = format_multiline(lines, tab)
    return result


def format_multiline(lines, tab):
    return '{\n' + ''.join(lines) + ' ' * 4 * tab + '}'
