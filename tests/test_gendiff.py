from gendiff.scripts.gendiff import generate_diff
import os


def write_temp_file(file_name, content):
    with open(file_name, 'w') as f:
        f.write(content)


def test_gendiff_equal_files():
    write_temp_file("file1.json", '{"key": "value"}')
    write_temp_file("file2.json", '{"key": "value"}')
    expected_result = "{\n    key: value\n}"
    assert generate_diff("file1.json", "file2.json") == expected_result


def test_gendiff_different_files():
    write_temp_file("file1.json", '{"key": "value1"}')
    write_temp_file("file2.json", '{"key": "value2"}')
    expected_result = "{\n  - key: value1\n  + key: value2\n}"
    assert generate_diff("file1.json", "file2.json") == expected_result


def test_gendiff_one_empty_file():
    write_temp_file("file1.json",'{"key": "value1"}')
    write_temp_file("file2.json",'{}')
    expected_result = "{\n  - key: value1\n}"
    assert generate_diff("file1.json", "file2.json") == expected_result


def test_gendiff_both_empty_files():
    write_temp_file("file1.json", '{}')
    write_temp_file("file2.json", '{}')
    expected_result = "{}"
    assert generate_diff("file1.json", "file2.json") == expected_result
