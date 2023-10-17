import pytest
from gendiff import diffgenerator

with open('./tests/fixtures/expected_results/stylish-flat.txt', mode='r') as file:
    expected = file.read()

file_path_1 = './tests/fixtures/trees/file1.json'
file_path_2 = './tests/fixtures/trees/file2.json'


@pytest.mark.parametrize('file_path_1, file_path_2, expected',
                         [(file_path_1, file_path_2, expected)])
def test_generate_diff(file_path_1, file_path_2, expected):
    assert (diffgenerator.generate_diff(file_path_1, file_path_2) == expected)
