from gendiff import constans as cons


def format_value(value, depth=0):
    if isinstance(value, dict):
        indent = '    ' * (depth + cons.DEPTH_INCREMENT)
        lines = ['{']
        for k, v in value.items():
            lines.append(f"{indent}{k}: {format_value(v, depth + cons.DEPTH_INCREMENT)}")
        lines.append('    ' * depth + '}')
        return '\n'.join(lines)
    elif isinstance(value, bool):
        return str(value).lower()
    elif isinstance(value, str) and value == "":
        return ""
    elif value is None:
        return 'null'
    return str(value)