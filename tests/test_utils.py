from gendiff.utils import parsing, read_file
from pathlib import Path


def get_fixture_path(filename):
    fixtures_folder = Path("tests") / "fixtures"
    return fixtures_folder / filename


def test_parsing():
    parsed_data1 = parsing.parse('{"a": 1}', format='json')
    parsed_data2 = parsing.parse('{"a": 1}', format='yaml')
    data, format = read_file.get_contents_suffix(get_fixture_path('file1.json'))
    parsed_data3 = parsing.parse(data, format)
    
    assert parsed_data1 == {"a": 1}
    assert parsed_data2 == {"a": 1}
    assert parsed_data3 == {
        "host": "hexlet.io",
        "timeout": 50,
        "proxy": "123.234.53.22",
        "follow": False
    }


def test_read_file():
    data, format = read_file.get_contents_suffix(get_fixture_path('file1.json'))

    assert format == 'json'
    assert data == '''{
    "host": "hexlet.io",
    "timeout": 50,
    "proxy": "123.234.53.22",
    "follow": false
}'''
