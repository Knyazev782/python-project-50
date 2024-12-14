def format_value(value, depth):
    if isinstance(value, dict):
        indent = "    " * (depth + 1)
        lines = [f"{indent}{key}: {format_value(val, depth + 1)}"
                 for key, val in value.items()]
        return "{\n" + "\n".join(lines) + f"\n{'    ' * depth}}}"
    elif isinstance(value, bool):
        return str(value).lower()
    elif value is None:
        return "null"
    return str(value)
