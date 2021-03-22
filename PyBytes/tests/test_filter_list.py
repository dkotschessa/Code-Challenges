
import pytest
from filter_list import filter_positive_even_numbers


params = [
    (
        [1,2,3,4,4,5], [2,4,4]
    ),
    (
        [-6,-3, -2, -1, 0 , 1, 2, 3, 4], [2,4]
    ),
    (
     [123,123, -124], []
    ),
    ]

@pytest.mark.parametrize("input, expected", params)
def test_filter(input, expected):
    result = filter_positive_even_numbers(input)
    assert result == expected