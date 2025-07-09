from gendiff.core.build_diff import build_diff
from gendiff import constans as cons


def test_build_diff_simple():
    dict1 = {"a": 1, "b": 2}
    dict2 = {"b": 2, "c": 3}
    result = build_diff(dict1, dict2)
    expected = [
        {'key': 'a', 'status': cons.REMOVED, 'value': 1},
        {'key': 'b', 'status': cons.UNCHANGED, 'value': 2},
        {'key': 'c', 'status': cons.ADDED, 'value': 3},
    ]
    assert result == expected


def test_build_diff_nested():
    dict1 = {"a": {"x": 1}, "b": 2}
    dict2 = {"a": {"x": 2}, "b": 2}
    result = build_diff(dict1, dict2)
    expected = [
        {
            'key': 'a',
            'status': cons.NESTED,
            'children': [{'key': 'x', 'status': cons.CHANGED,
                          'old_value': 1, 'new_value': 2}]
        },
        {'key': 'b', 'status': cons.UNCHANGED, 'value': 2},
    ]
    assert result == expected
