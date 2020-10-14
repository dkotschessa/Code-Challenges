import pytest
import max_profit


params = [([[7,1,5,3,6,4]], 7),
           ([1,2,3,4,5], 4),
           ([7,6,4,3,1], 0)]

@pytest.mark.parametrize("input, expected", params)
def test_max_profit(input, expected):
    assert maxProfit(input) == expected