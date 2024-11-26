from gendiff.scripts.gendiff import generate_diff


def test_gendiff_equal_files(tmp_path):
    file1 = tmp_path / "file1.yml"
    file2 = tmp_path / "file2.yml"
    file1.write_text("""
    key: value
    """)
    file2.write_text("""
    key: value
    """)
    expected_result = "{\n    key: value\n}"
    assert generate_diff(str(file1), str(file2)) == expected_result


def test_gendiff_different_files(tmp_path):
    file1 = tmp_path / "file1.yml"
    file2 = tmp_path / "file2.yml"
    file1.write_text("""
    key: value1
    """)
    file2.write_text("""
    key: value2
    """)
    expected_result = "{\n  - key: value1\n  + key: value2\n}"
    assert generate_diff(str(file1), str(file2)) == expected_result


def test_gendiff_one_empty_file(tmp_path):
    file1 = tmp_path / "file1.yml"
    file2 = tmp_path / "file2.yml"
    file1.write_text("""
    key: value1
    """)
    file2.write_text("{}")
    expected_result = "{\n  - key: value1\n}"
    assert generate_diff(str(file1), str(file2)) == expected_result


def test_gendiff_both_empty_files(tmp_path):
    file1 = tmp_path / "file1.yml"
    file2 = tmp_path / "file2.yml"
    file1.write_text("{}")
    file2.write_text("{}")
    expected_result = "{}"
    assert generate_diff(str(file1), str(file2)) == expected_result
