from gendiff.core.format_value import format_value


def test_format_value():
    assert format_value(True, 0) == "true"
    assert format_value(False, 0) == "false"
    assert format_value(None, 0) == "null"
    assert format_value("string", 0) == "string"
    assert format_value(123, 0) == "123"
    assert format_value({"key": "value"}, 0) == "{\n    key: value\n}"
