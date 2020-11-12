import pytest
from shuffle_array import shuffleArray


params = [
    (
        [2,5,1,3,4,7], [2,3,5,4,1,7]
    ),
    (
        [1,2,3,4,4,3,2, 1], [1,4,2,3,3,2,4,1]
    ),
    (
        [1,1,2,2], [1,2,1,2]
    )
           ]

@pytest.mark.parametrize("input, expected", params)
def test_shuffle_array(input, expected):
    assert shuffleArray(input) == expected