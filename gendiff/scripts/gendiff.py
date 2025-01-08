from gendiff.scripts.parsing_files import get_parse_file
from gendiff.scripts.build_diff import build_diff
import argparse
from gendiff.formatters.format_plain import format_plain
from gendiff.formatters.format_stylish import format_stylish


def generate_diff(file_path1, file_path2, format='stylish'):
    data1 = get_parse_file(file_path1)
    data2 = get_parse_file(file_path2)
    diff = build_diff(data1, data2)
    if format == 'plain':
        return format_plain(diff)
    elif format == 'stylish':
        return format_stylish(diff)


def main():
    parser = argparse.ArgumentParser(description='Generate diff for two files.')
    parser.add_argument('first_file', type=str, help='Path to the first file')
    parser.add_argument('second_file', type=str, help='Path to the second file')
    parser.add_argument(
        '-f', '--format',
        default='stylish',
        help='Set format of output (default: stylish)'
    )
    args = parser.parse_args()
    diff = generate_diff(args.first_file, args.second_file, format=args.format)
    print(diff)
