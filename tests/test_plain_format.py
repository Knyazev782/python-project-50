import json
from pathlib import Path
import pytest
from gendiff.formatters.format_plain import format_plain
from gendiff.core.build_diff import build_diff

FIXTURES_PATH = Path(__file__).parent / 'fixtures'

def load_fixture(name):
    with open(FIXTURES_PATH / name) as f:
        return f.read().strip()

@pytest.fixture
def complex_diff():
    with open(FIXTURES_PATH / 'file1.json') as f1, open(FIXTURES_PATH / 'file2.json') as f2:
        file1 = json.load(f1)
        file2 = json.load(f2)
        return build_diff(file1, file2)

def test_format_plain(complex_diff):
    result = format_plain(complex_diff)
    expected = load_fixture('plain_result')
    assert result == expected