from gendiff.core.format_value import format_value
from gendiff import constans as cons

SIGN_MAP = {
    cons.ADDED: '  + ',
    cons.REMOVED: '  - ',
    cons.UNCHANGED: '    '
}

def format_stylish(diff, depth=0):
    if not diff:
        return '{}'

    indent = '    ' * depth
    lines = ['{']

    for item in diff:
        key = item['key']
        status = item['status']
        current_indent = indent + '    '

        if status == cons.NESTED:
            value = format_stylish(item['children'], depth + cons.DEPTH_INCREMENT)
            lines.append(f"{current_indent}{key}: {value}")
        elif status == cons.CHANGED:
            old_val = format_value(item['old_value'], depth + cons.DEPTH_INCREMENT)
            new_val = format_value(item['new_value'], depth + cons.DEPTH_INCREMENT)
            if item['old_value'] == "":
                lines.append(f"{indent}  - {key}:")
            else:
                lines.append(f"{indent}  - {key}: {old_val}")
            lines.append(f"{indent}  + {key}: {new_val}")
        else:
            value = format_value(item['value'], depth + cons.DEPTH_INCREMENT)
            if item.get('value') == "":
                lines.append(f"{indent}{SIGN_MAP[status]}{key}:")
            else:
                lines.append(f"{indent}{SIGN_MAP[status]}{key}: {value}")

    lines.append(f"{indent}}}")
    return '\n'.join(lines)