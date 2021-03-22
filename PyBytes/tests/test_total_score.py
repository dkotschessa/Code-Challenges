
import pytest
from collections import namedtuple
from total_score import get_total_points

BeltStats = namedtuple('BeltStats', 'score ninjas')
from filter_list import filter_positive_even_numbers

ninja_belts = {'yellow': BeltStats(50, 11),
               'orange': BeltStats(100, 7),
               'green': BeltStats(175, 1),
               'blue': BeltStats(250, 5)}

more_belts = dict(brown=BeltStats(400, 2),
                  black=BeltStats(600, 5))

ninja_belts_updated = {**ninja_belts, **more_belts}

nothing_belts = {'yellow': BeltStats(0,0)}

params = [
    (
        ninja_belts, 2675
    ),
    (
        ninja_belts_updated, 6475
    ),
    (
        nothing_belts, 0
    ),
    ]

@pytest.mark.parametrize("input, expected", params)
def test_filter(input, expected):
    result = get_total_points(input)
    assert result == expected