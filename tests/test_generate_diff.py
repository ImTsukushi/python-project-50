from gendiff.diffgenerator import generate_diff
result = '''{
- follow: False
  host: hexlet.io
- proxy: 123.234.53.22
- timeout: 50
+ timeout: 20
+ verbose: True
}'''
file_path_1 = './tests/fixtures/file1.json'
file_path_2 = './tests/fixtures/file2.json'


def test_generate_diff():
    assert (generate_diff(file_path_1, file_path_2) == result)
