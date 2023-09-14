from gendiff.scripts.gendiff import generate_diff
from pathlib import Path


def test_generate_diff():
    fixtures_folder = Path('gendiff') / 'tests' / 'fixtures'
    diff = generate_diff(
        fixtures_folder / 'file1.json', fixtures_folder / 'file2.json'
        )
    with open(fixtures_folder / 'result.txt') as result_file:
        result = result_file.read()
    assert result == diff
