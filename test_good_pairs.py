import pytest
from good_pairs import goodPairs


params = [
    (
        [1,2,3,1,1,3], 4
    ),
    (
        [1,1,1,1], 6
    ),
    (
        [1,2,3], 0
    )
           ]

@pytest.mark.parametrize("input, expected", params)
def test_good_pairs(input, expected):
    assert goodPairs(input) == expected