from gendiff.scripts.gendiff import generate_diff
from pathlib import Path


def get_fixture_path(filename):
    fixtures_folder = Path('gendiff') / 'tests' / 'fixtures'
    return fixtures_folder / filename


def test_generate_diff_json():
    diff = generate_diff(
        get_fixture_path('file1.json'), get_fixture_path('file2.json')
    )
    with open(get_fixture_path('result_stylish.txt')) as result_file:
        result = result_file.read()
    assert result == diff


def test_generate_diff_yml():
    diff = generate_diff(
        get_fixture_path('file1.yml'), get_fixture_path('file2.yml')
    )
    with open(get_fixture_path('result_stylish.txt')) as result_file:
        result = result_file.read()
    assert result == diff


def test_generate_diff_nested_json():
    diff = generate_diff(
        get_fixture_path('nested_file1.json'),
        get_fixture_path('nested_file2.json')
    )

    with open(get_fixture_path('nested_result_stylish.txt')) as result_file:
        result = result_file.read()
    assert result == diff

def test_generate_diff_nested_yml():
    diff = generate_diff(
        get_fixture_path('nested_file1.yml'),
        get_fixture_path('nested_file2.yaml')
    )

    with open(get_fixture_path('nested_result_stylish.txt')) as result_file:
        result = result_file.read()
    assert result == diff