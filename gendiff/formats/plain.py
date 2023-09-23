def format_diff_plain(diff, parent_key=''):
    text = []
    for entry in diff:
        text.append(format_entry(entry, parent_key))
    return '\n'.join([line for line in text if line])


def format_entry(entry, parent_key):
    key = parent_key + entry['key']
    old_value = format_value(entry.get('old_value'))
    new_value = format_value(entry.get('new_value'))
    state = entry['state']

    if state == 'added':
        result = f"Property '{key}' was added with value: {new_value}"
    elif state == 'deleted':
        result = f"Property '{key}' was removed"
    elif state == 'changed':
        result = f"Property '{key}' was updated."
        result += f" From {old_value} to {new_value}"
    elif state == 'nested':
        result = format_diff_plain(entry['children'], f"{key}.")
    return result


def format_value(value):
    result = value
    if isinstance(value, bool):
        result = str(value).lower()
    elif value is None:
        result = 'null'
    elif isinstance(value, dict) or isinstance(value, list):
        result = '[complex value]'
    elif isinstance(value, str):
        result = f"'{value}'"
    return result
