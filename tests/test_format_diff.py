from gendiff.formatters.format_stylish import format_stylish

ADDED = "added"
REMOVED = "removed"
CHANGED = "changed"
UNCHANGED = "unchanged"
NESTED = "nested"


def test_format_stylish_simple():
    diff = [
        {'key': 'a', 'status': REMOVED, 'value': 1},
        {'key': 'b', 'status': UNCHANGED, 'value': 2},
        {'key': 'c', 'status': ADDED, 'value': 3},
    ]
    result = format_stylish(diff)
    expected = "{\n  - a: 1\n    b: 2\n  + c: 3\n}"
    assert result == expected


def test_format_stylish_nested():
    diff = [
        {
            'key': 'a',
            'status': NESTED,
            'children': [{'key': 'x', 'status': CHANGED,
                          'old_value': 1, 'new_value': 2}]
        },
    ]
    result = format_stylish(diff)
    expected = "{\n    a: {\n      - x: 1\n      + x: 2\n    }\n}"
    assert result == expected
