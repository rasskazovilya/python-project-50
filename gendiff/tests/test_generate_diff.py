from gendiff.scripts.gendiff import generate_diff
from pathlib import Path


def get_fixture_path(filename):
    fixtures_folder = Path('gendiff') / 'tests' / 'fixtures'
    return fixtures_folder / filename


def test_generate_diff():
    diff = generate_diff(
        get_fixture_path('file1.json'), get_fixture_path('file2.json')
    )
    with open(get_fixture_path('result.txt')) as result_file:
        result = result_file.read()
    assert result == diff
