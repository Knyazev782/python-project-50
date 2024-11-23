import argparse
import json


def read_json_file(address_file):
    with open(address_file, 'r') as file:
        return json.load(file)


def generate_diff(path_file1, path_file2):
    result = []
    read_file1 = read_json_file(path_file1)
    read_file2 = read_json_file(path_file2)
    keys = sorted(read_file1.keys() | read_file2.keys())
    for key in keys:
        if key in read_file1 and key in read_file2:
            if read_file1[key] == read_file2[key]:
                result.append(f"    {key}: {read_file1[key]}")
            else:
                result.append(f"  - {key}: {read_file1[key]}")
                result.append(f"  + {key}: {read_file2[key]}")
        elif key in read_file1:
            result.append(f"  - {key}: {read_file1[key]}")
        elif key in read_file2:
            result.append(f"  + {key}: {read_file2[key]}")
    if not result:
        return "{}"
    return "{\n" + "\n".join(result) + "\n}"


def main():
    parser = argparse.ArgumentParser(
        description="Compares two configuration files and shows a difference."
    )
    parser.add_argument('first_file', help="Path to the first JSON file.")
    parser.add_argument('second_file', help="Path to the second JSON file.")
    parser.add_argument('-f', '--format', dest='FORMAT',
                        help='Set format of output (not implemented yet)')
    args = parser.parse_args()
    diff = generate_diff(args.first_file, args.second_file)
    print(diff)


if __name__ == "__main__":
    main()
