import json
from pathlib import Path
import pytest
from gendiff.gendiff import generate_diff

FIXTURES_PATH = Path(__file__).parent / 'fixtures'

def load_fixture(name):
    with open(FIXTURES_PATH / name) as f:
        return f.read().strip()

@pytest.fixture
def file1_json():
    return FIXTURES_PATH / 'file1.json'

@pytest.fixture
def file2_json():
    return FIXTURES_PATH / 'file2.json'

def test_generate_diff_stylish(file1_json, file2_json):
    result = generate_diff(file1_json, file2_json)
    expected = load_fixture('stylish_result')
    assert result == expected

def test_generate_diff_plain(file1_json, file2_json):
    result = generate_diff(file1_json, file2_json, format='plain')
    expected = load_fixture('plain_result')
    assert result == expected

def test_generate_diff_json(file1_json, file2_json):
    result = generate_diff(file1_json, file2_json, format='json')
    expected = load_fixture('json_result.json')
    assert json.loads(result) == json.loads(expected)