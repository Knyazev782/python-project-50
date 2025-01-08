from gendiff.formatters.format_stylish import format_stylish
from gendiff.formatters.format_plain import format_plain

FORMATTERS = {
    'stylish': format_stylish,
    'plain': format_plain,
}

def get_formatter(name):
    return FORMATTERS[name]
