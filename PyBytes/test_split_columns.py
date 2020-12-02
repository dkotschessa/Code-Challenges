import pytest
from split_columns import split_in_columns

input1 = "Hello world:\nI am coding in Python :)\nHow awesome!"
expected1 = "Hello world:|I am coding in Python :)|How awesome!"

input2 = "this\n is \n a\n lot\n of\n newlines\n"
expected2 = "this| is | a| lot| of| newlines|"

input3 = "\n\n\n\n\n"
expected3 = "|||||"

params = [
    (
        input1, expected1
    ),
    (
         input2, expected2
    ),
    (
        input3, expected3
    ),
           ]

@pytest.mark.parametrize("input, expected", params)
def test_split_in_columns(input, expected):
    result = split_in_columns(input)
    assert result == expected
