ADDED = "added"
REMOVED = "removed"
CHANGED = "changed"
UNCHANGED = "unchanged"
NESTED = "nested"


def format_plain(diff, parent=''):
    def process_node(node, path):
        status = node['status']
        if status == ADDED:
            return format_added(path, node['value'])
        elif status == REMOVED:
            return format_removed(path)
        elif status == CHANGED:
            return format_changed(path, node['old_value'], node['new_value'])
        elif status == NESTED:
            return format_nested(node['children'], path)
        return None

    def format_added(path, value):
        formatted_value = format_value(value)
        return f"Property '{path}' was added with value: {formatted_value}"

    def format_removed(path):
        return f"Property '{path}' was removed"

    def format_changed(path, old_value, new_value):
        formatted_old = format_value(old_value)
        formatted_new = format_value(new_value)
        return (
            f"Property '{path}' was updated. "
            f"From {formatted_old} to {formatted_new}"
        )

    def format_nested(children, path):
        return format_plain(children, path)

    lines = []
    if isinstance(diff, list):
        for node in diff:
            key = node['key']
            path = f"{parent}.{key}" if parent else key
            line = process_node(node, path)
            if line:
                lines.append(line)
    else:
        for key, node in diff.items():
            path = f"{parent}.{key}" if parent else key
            line = process_node(node, path)
            if line:
                lines.append(line)
    return '\n'.join(lines)


def format_value(value):
    if isinstance(value, dict):
        return '[complex value]'
    elif isinstance(value, bool):
        return str(value).lower()
    elif value is None:
        return 'null'
    elif isinstance(value, str):
        return f"'{value}'"
    return str(value)
