from gendiff.core.parsing_files import get_parse_file
from gendiff.core.build_diff import build_diff
from gendiff.formatters.format_plain import format_plain
from gendiff.formatters.format_stylish import format_stylish
from gendiff.formatters.format_json import format_json
from gendiff.init_parser.parser import init_parser

FORMATTER_MAPS = {'stylish': format_stylish,
                  'plain': format_plain,
                  'json': format_json
                  }


def generate_diff(file_path1, file_path2, format='stylish'):
    file1 = get_parse_file(file_path1)
    file2 = get_parse_file(file_path2)
    diff = build_diff(file1, file2)
    return FORMATTER_MAPS[format](diff)


def main():
    parser = init_parser()
    args = parser.parse_args()
    diff = generate_diff(args.first_file, args.second_file, format=args.format)
    print(diff)


if __name__ == '__main__':
    main()
