import pytest
from string_shuffle import stringShuffle


params = [
    (
        "codeleet", [4,5,6,7,0,2,1,3], "leetcode"
    ),
    (
        "abc", [0,1,2], "abc"
    ),
    (
        "aiohn", [3,1,4,2,0], "nihao"
    ),
    (
        "aaiougrt", [4,0,2,6,7,3,1,5], "arigatou"
    )
           ]

@pytest.mark.parametrize("input1, input2, expected", params)
def test_string_shuffle(input1, input2, expected):
    assert stringShuffle(input1, input2) == expected