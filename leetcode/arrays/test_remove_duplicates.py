import pytest
from remove_duplicates import removeDuplicates

params = [([1,2,2], 2),
           ([0,0,1,1,1,2,2,3,3,4], 5),
           ([1,1,1,1], 1)]


@pytest.mark.parametrize("input, expected", params)
def test_remove_duplicates(input, expected):
    assert removeDuplicates(input) == expected

