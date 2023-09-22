def format_diff_stylish(diff):
    text = ''.join(map(format_entry, diff))
    return '{\n' + text + '}'


def format_entry(entry, tab=1):
    key = entry.get('key')
    old = entry.get('old_value')
    new = entry.get('new_value')
    children = entry.get('children')

    operations = {
        'added': lambda _, value: format_line(key, value, '+', tab),
        'deleted': lambda value, _: format_line(key, value, '-', tab),
        'changed': lambda old, new: format_changed(key, old, new, tab),
        'unchanged': lambda value, _: format_line(key, value, ' ', tab),
        'nested': lambda children, _: format_line(key, children, ' ', tab),
    }

    if entry['state'] == 'nested':
        return operations[entry['state']](children, None)
    return operations[entry['state']](old, new)


def format_changed(key, old, new, tab):
    return (
        format_line(key, old, '-', tab) +
        format_line(key, new, '+', tab)
    )


def format_line(key, value, op, tab):
    indent = ' ' * (4 * tab - 2)
    text = format_value(value, tab)
    return f'{indent}{op} {key}: {text}\n'


def format_value(value, tab):
    if value is True:
        return 'true'
    elif value is False:
        return 'false'
    elif value is None:
        return 'null'
    elif isinstance(value, dict):
        lines = [format_line(k, v, ' ', tab + 1) for k, v in value.items()]
        return format_multiline(lines, tab)
    elif isinstance(value, list):
        lines = [format_entry(v, tab + 1) for v in value]
        return format_multiline(lines, tab)
    else:
        return value


def format_multiline(lines, tab):
    return f'{"{"}\n' + ''.join(lines) + ' ' * 4 * tab + '}'
