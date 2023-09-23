def format_diff_plain(diff, parent_key=''):
    text = []
    for entry in diff:
        text.append(format_entry(entry, parent_key))
    return '\n'.join([line for line in text if line])


def format_entry(entry, parent_key):
    key = parent_key + entry['key']
    old_value = format_value(entry.get('old_value'))
    new_value = format_value(entry.get('new_value'))

    if entry['state'] == 'added':
        return f"Property '{key}' was added with value: {new_value}"
    elif entry['state'] == 'deleted':
        return f"Property '{key}' was removed"
    elif entry['state'] == 'changed':
        result = f"Property '{key}' was updated."
        return result + f" From {old_value} to {new_value}"
    elif entry['state'] == 'nested':
        return format_diff_plain(entry['children'], f"{key}.")
    else:
        return ''


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
        return f"'{value}'"
    else:
        return value
