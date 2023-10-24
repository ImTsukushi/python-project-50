import pytest
from gendiff import generate_diff


json_flat_1 = './tests/fixtures/trees/nestedfile1.json'
json_flat_2 = './tests/fixtures/trees/nestedfile2.json'
expected = './tests/fixtures/expected_results/stylish-nested.txt'


@pytest.mark.parametrize('file_path_1, file_path_2, expected',
                         [
                             (json_flat_1, json_flat_2, expected),
                         ])
def test_generate_diff(file_path_1, file_path_2, expected):
    with open(expected, mode='r') as file:
        assert generate_diff(file_path_1, file_path_2) == file.read()
