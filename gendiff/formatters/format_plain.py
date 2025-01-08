ADDED = "added"
REMOVED = "removed"
CHANGED = "changed"
UNCHANGED = "unchanged"
NESTED = "nested"


def format_plain(diff, parent=''):
    lines = []
    if isinstance(diff, list):
        for node in diff:
            key = node['key']
            path = f"{parent}.{key}" if parent else key
            status = node['status']
            if status == ADDED:
                value = format_value(node['value'])
                lines.append(f"Property '{path}' was added with value: {value}")
            elif status == REMOVED:
                lines.append(f"Property '{path}' was removed")
            elif status == CHANGED:
                old_value = format_value(node['old_value'])
                new_value = format_value(node['new_value'])
                lines.append(f"Property '{path}' was updated. From {old_value} to {new_value}")
            elif status == NESTED:
                lines.append(format_plain(node['children'], path))
    else:
        for key, node in diff.items():
            path = f"{parent}.{key}" if parent else key
            status = node['status']
            if status == ADDED:
                value = format_value(node['value'])
                lines.append(f"Property '{path}' was added with value: {value}")
            elif status == REMOVED:
                lines.append(f"Property '{path}' was removed")
            elif status == CHANGED:
                old_value = format_value(node['old_value'])
                new_value = format_value(node['new_value'])
                lines.append(f"Property '{path}' was updated. From {old_value} to {new_value}")
            elif status == NESTED:
                lines.append(format_plain(node['children'], path))
    return '\n'.join(lines)


def format_value(value):
    if isinstance(value, dict) or isinstance(value, list):
        return '[complex value]'
    if isinstance(value, bool):
        return 'true' if value else 'false'
    if value is None:
        return 'null'
    if isinstance(value, str):
        return f"'{value}'"
    return str(value)
