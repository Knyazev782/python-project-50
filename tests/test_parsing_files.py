import json
from pathlib import Path
import pytest
from gendiff.core.parsing_files import get_parse_file

FIXTURES_PATH = Path(__file__).parent / 'fixtures'


def test_parse_json():
    data = get_parse_file(FIXTURES_PATH / 'file1.json')
    assert data['common']['setting1'] == 'Value 1'
    assert data['group1']['baz'] == 'bas'


def test_parse_yaml():
    data = get_parse_file(FIXTURES_PATH / 'file1.yml')
    assert data['common']['setting1'] == 'Value 1'
    assert data['group1']['baz'] == 'bas'


def test_parse_unsupported_format(tmp_path):
    unsupported = tmp_path / 'file.txt'
    unsupported.write_text('test')
    with pytest.raises(ValueError):
        get_parse_file(unsupported)
