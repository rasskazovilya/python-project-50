def format_diff_plain(diff, parent_key=''):
    text = []
    if parent_key:
        parent_key += '.'
    for entry in diff:
        key = entry['key']
        old_value = entry.get('old_value')
        new_value = entry.get('new_value')

        if entry['state'] == 'added':
            text.append(add_line(parent_key + key, new_value))
        elif entry['state'] == 'deleted':
            text.append(remove_line(parent_key + key))
        elif entry['state'] == 'changed':
            text.append(update_line(parent_key + key, old_value, new_value))
        elif entry['state'] == 'nested':
            text.append(format_diff_plain(entry['children'], parent_key + key))

    return '\n'.join(text)


def add_line(key, new_value):
    new_value = format_value(new_value)
    return f"Property '{key}' was added with value: {new_value}"


def update_line(key, old_value, new_value):
    old_value = format_value(old_value)
    new_value = format_value(new_value)
    return f"Property '{key}' was updated. From {old_value} to {new_value}"


def remove_line(key):
    return f"Property '{key}' was removed"


def format_value(value):
    if value is True:
        return 'true'
    elif value is False:
        return 'false'
    elif value is None:
        return 'null'
    elif isinstance(value, dict) or isinstance(value, list):
        return '[complex value]'
    elif isinstance(value, str):
        return f'\'{value}\''
