def format_diff_stylish(diff):
    text = format_diff(diff)
    return '{\n' + text + '}'


def format_diff(diff, tab=1):
    text = ''
    for entry in diff:
        key = entry['key']
        old_value = entry.get('old_value')
        new_value = entry.get('new_value')
        children = entry.get('children')

        if entry['state'] == 'added':
            text += format_line(key, new_value, '+', tab)
        elif entry['state'] == 'deleted':
            text += format_line(key, old_value, '-', tab)
        elif entry['state'] == 'changed':
            text += format_line(key, old_value, '-', tab)
            text += format_line(key, new_value, '+', tab)
        elif entry['state'] == 'unchanged':
            text += format_line(key, new_value, ' ', tab)
        elif entry['state'] == 'nested':
            text += format_line(key, children, ' ', tab)
    return text


def format_line(key, value, op, tab):
    indent = ' ' * (4 * tab - 2)
    text = format_value(value)
    if isinstance(value, dict):
        # print(key, value)
        text = f'{indent}{op} {key}: {"{"}\n'
        text += ''.join(format_line(k, v, ' ', tab + 1) for k, v in value.items())
        # for k, v in value.items():
        #     text += format_line(k, v, ' ', tab + 1)
        return text + ' ' * 4 * tab + '}\n'
    elif isinstance(value, list):
        text = f'{indent}{op} {key}: {"{"}\n'
        text += format_diff(value, tab + 1)
        return text + ' ' * 4 * tab + '}\n'
    return f'{indent}{op} {key}: {format_value(value)}\n'


def format_value(value):
    if value is True:
        return 'true'
    elif value is False:
        return 'false'
    elif value is None:
        return 'null'
    # elif isinstance(value, dict):
    #     return ''.join(format_line(k, v, ' ', tab + 1) for k, v in value.items())
    else:
        return value
