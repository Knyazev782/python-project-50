from gendiff.scripts.build_diff import build_diff
from gendiff.scripts.format_diff import format_stylish
from gendiff.scripts.parsing_files import get_parse_file
import argparse


def generate_diff(file_path1, file_path2):
    file_data1 = get_parse_file(file_path1)
    file_data2 = get_parse_file(file_path2)
    diff = build_diff(file_data1, file_data2)
    return format_stylish(diff)


def main():
    parser = (argparse.ArgumentParser
              (description='Generate diff for two files.'))
    parser.add_argument('first_file', type=str, help='Path to the first file')
    parser.add_argument('second_file',
                        type=str, help='Path to the second file')
    parser.add_argument('-f', '--format',
                        default='stylish', help='Set format of output')
    args = parser.parse_args()
    diff = generate_diff(args.first_file, args.second_file)
    print(diff)
