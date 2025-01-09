from gendiff.scripts.gendiff import generate_diff


def test_generate_diff_json(tmp_path):
    file1_path = tmp_path / "file1.json"
    file2_path = tmp_path / "file2.json"
    file1_content = '{"a": 1, "b": 2}'
    file2_content = '{"b": 2, "c": 3}'
    file1_path.write_text(file1_content)
    file2_path.write_text(file2_content)
    expected = "{\n  - a: 1\n    b: 2\n  + c: 3\n}"
    assert generate_diff(str(file1_path), str(file2_path)) == expected


def test_generate_diff_yaml(tmp_path):
    file1_path = tmp_path / "file1.yaml"
    file2_path = tmp_path / "file2.yaml"
    file1_content = "a: 1\nb: 2\n"
    file2_content = "b: 2\nc: 3\n"
    file1_path.write_text(file1_content)
    file2_path.write_text(file2_content)
    expected = "{\n  - a: 1\n    b: 2\n  + c: 3\n}"
    assert generate_diff(str(file1_path), str(file2_path)) == expected


def test_generate_diff_nested(tmp_path):
    file1_path = tmp_path / "file1.json"
    file2_path = tmp_path / "file2.json"
    file1_path.write_text('{"a": {"x": 1}, "b": 2}')
    file2_path.write_text('{"a": {"x": 2}, "b": 2, "c": 3}')
    expected = """{
    a: {
      - x: 1
      + x: 2
    }
    b: 2
  + c: 3
}"""
    assert generate_diff(str(file1_path), str(file2_path)) == expected


def test_generate_diff_empty(tmp_path):
    file1_path = tmp_path / "file1.json"
    file2_path = tmp_path / "file2.json"
    file1_path.write_text("{}")
    file2_path.write_text("{}")
    expected = "{}"
    assert generate_diff(str(file1_path), str(file2_path)) == expected


def test_generate_diff_plain(tmp_path):
    file1_path = tmp_path / "file1.json"
    file2_path = tmp_path / "file2.json"
    file1_path.write_text('{"key1": "value1"}')
    file2_path.write_text('{"key1": "value2", "key2": "value3"}')

    expected = (
        "Property 'key1' was updated. From 'value1' to 'value2'\n"
        "Property 'key2' was added with value: 'value3'"
    )

    result = generate_diff(str(file1_path), str(file2_path), format='plain')
    assert result == expected


def test_format_json():
    diff = {
        'key1': {'status': 'changed',
                 'old_value': 'value1', 'new_value': 'value2'},
        'key2': {'status': 'added', 'value': 'value3'},
    }

    expected = (
        '{\n'
        '    "key1": {\n'
        '        "status": "changed",\n'
        '        "old_value": "value1",\n'
        '        "new_value": "value2"\n'
        '    },\n'
        '    "key2": {\n'
        '        "status": "added",\n'
        '        "value": "value3"\n'
        '    }\n'
        '}'
    )

    assert generate_diff(diff, {}, format='json') == expected
