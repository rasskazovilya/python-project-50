from gendiff.scripts.gendiff import generate_diff
from pathlib import Path
import pytest


def get_fixture_path(filename):
    fixtures_folder = Path("tests") / "fixtures"
    return fixtures_folder / filename


@pytest.mark.parametrize(
    ["file1", "file2", "format"],
    [
        ("file1.json", "file2.json", "stylish"),
        ("file1.yml", "file2.yml", "stylish"),
        ("nested_file1.json", "nested_file2.json", "stylish"),
        ("nested_file1.yml", "nested_file2.yaml", "stylish"),
        ("nested_file1.json", "nested_file2.json", "plain"),
        ("nested_file1.yml", "nested_file2.yaml", "plain"),
        ("nested_file1.json", "nested_file2.json", "json"),
        ("nested_file1.yml", "nested_file2.yaml", "json"),
    ],
)
def test_gendiff(file1, file2, format):
    diff = generate_diff(get_fixture_path(file1), get_fixture_path(file2), format)

    result_path = f"result_{format}.txt"
    if "nested" in file1:
        result_path = "nested_" + result_path

    with open(get_fixture_path(result_path)) as result_file:
        result = result_file.read()
    assert result == diff
