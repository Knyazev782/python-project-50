import argparse


def init_parser():
    parser = argparse.ArgumentParser(
        description='Generate diff for two files.')
    parser.add_argument('first_file',
                        type=str,
                        help='Path to the first file')
    parser.add_argument('second_file',
                        type=str,
                        help='Path to the second file')
    parser.add_argument(
        '-f', '--format',
        default='stylish',
        help='Set format of output (default: stylish)'
    )
    return parser