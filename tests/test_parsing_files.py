import tempfile
import json
from gendiff.scripts.parsing_files import get_parse_file


def test_get_parse_file_json():
    with tempfile.NamedTemporaryFile(mode='w', suffix='.json',
                                     delete=False) as temp_file:
        temp_file.write(json.dumps({"key": "value"}))
        temp_file_path = temp_file.name
    result = get_parse_file(temp_file_path)
    assert result == {"key": "value"}


def test_get_parse_file_yaml():
    with tempfile.NamedTemporaryFile(mode='w', suffix='.yaml',
                                     delete=False) as temp_file:
        temp_file.write("key: value\n")
        temp_file_path = temp_file.name
    result = get_parse_file(temp_file_path)
    assert result == {"key": "value"}
