from gendiff.scripts.format_value import format_value

ADDED = "added"
REMOVED = "removed"
CHANGED = "changed"
UNCHANGED = "unchanged"
NESTED = "nested"


def format_stylish(diff, depth=0):
    if not diff:
        return "{}"
    indent = "    " * depth
    result = ["{"]
    for item in diff:
        key = item['key']
        status = item['status']
        if status == ADDED:
            result.append(f"{indent}  + {key}: "
                          f"{format_value(item['value'], depth + 1)}")
        elif status == REMOVED:
            result.append(f"{indent}  - {key}: "
                          f"{format_value(item['value'], depth + 1)}")
        elif status == UNCHANGED:
            result.append(f"{indent}    {key}: "
                          f"{format_value(item['value'], depth + 1)}")
        elif status == CHANGED:
            result.append(f"{indent}  - {key}: "
                          f"{format_value(item['old_value'], depth + 1)}")
            result.append(f"{indent}  + {key}: "
                          f"{format_value(item['new_value'], depth + 1)}")
        elif status == NESTED:
            result.append(f"{indent}    {key}: "
                          f"{format_stylish(item['children'], depth + 1)}")
    result.append(f"{indent}}}")
    return "\n".join(result)
