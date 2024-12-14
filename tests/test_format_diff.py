from gendiff.scripts.format_diff import format_stylish


def test_format_stylish_simple():
    diff = [
        {'key': 'a', 'status': 'removed', 'value': 1},
        {'key': 'b', 'status': 'unchanged', 'value': 2},
        {'key': 'c', 'status': 'added', 'value': 3},
    ]
    result = format_stylish(diff)
    expected = "{\n  - a: 1\n    b: 2\n  + c: 3\n}"
    assert result == expected


def test_format_stylish_nested():
    diff = [
        {
            'key': 'a',
            'status': 'nested',
            'children': [{'key': 'x', 'status': 'changed',
                          'old_value': 1, 'new_value': 2}]
        },
    ]
    result = format_stylish(diff)
    expected = "{\n    a: {\n      - x: 1\n      + x: 2\n    }\n}"
    assert result == expected
