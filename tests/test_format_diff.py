import json
from pathlib import Path
import pytest
from gendiff.formatters.format_stylish import format_stylish
from gendiff.core.build_diff import build_diff

FIXTURES_PATH = Path(__file__).parent / 'fixtures'

def load_fixture(name):
    with open(FIXTURES_PATH / name) as f:
        return f.read().strip()

@pytest.fixture
def simple_diff():
    with open(FIXTURES_PATH / 'simple_diff.json') as f:
        return json.load(f)

@pytest.fixture
def nested_diff():
    with open(FIXTURES_PATH / 'nested_diff.json') as f:
        return json.load(f)

def test_format_stylish_simple(simple_diff):
    result = format_stylish(simple_diff)
    expected = load_fixture('simple_stylish_result')
    assert result == expected

def test_format_stylish_nested(nested_diff):
    result = format_stylish(nested_diff)
    expected = load_fixture('nested_stylish_result')
    assert result == expected

def test_format_stylish_complex():
    with open(FIXTURES_PATH / 'file1.json') as f1, open(FIXTURES_PATH / 'file2.json') as f2:
        file1 = json.load(f1)
        file2 = json.load(f2)
        diff = build_diff(file1, file2)

    result = format_stylish(diff)
    expected = load_fixture('stylish_result')
    assert result == expected