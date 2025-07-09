from gendiff import constans as cons


def format_value(value):
    if isinstance(value, dict):
        return '[complex value]'
    elif isinstance(value, bool):
        return str(value).lower()
    elif value is None:
        return cons.NULL_REPRESENTATION
    elif isinstance(value, str):
        return f"'{value}'"
    return str(value)


def format_plain(diff, path=''):
    lines = []
    for node in diff:
        current_path = f"{path}.{node['key']}" if path else node['key']

        if node['status'] == cons.NESTED:
            nested_lines = format_plain(node['children'], current_path)
            if nested_lines:
                lines.append(nested_lines)
        elif node['status'] == cons.ADDED:
            value = format_value(node['value'])
            lines.append(f"Property '{current_path}' was added with value: {value}")
        elif node['status'] == cons.REMOVED:
            lines.append(f"Property '{current_path}' was removed")
        elif node['status'] == cons.CHANGED:
            old_value = format_value(node['old_value'])
            new_value = format_value(node['new_value'])
            lines.append(
                f"Property '{current_path}' was updated. "
                f"From {old_value} to {new_value}"
            )

    return '\n'.join(lines)