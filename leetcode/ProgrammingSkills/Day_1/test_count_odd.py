from .count_odd import Solution


def test_count_odds():
    low = 3
    high = 7
    solution = Solution()
    result = solution.countOdds(low, high)
    assert result == 3


def test_count_odds_2():
    low = 8
    high = 10
    solution = Solution()
    result = solution.countOdds(low, high)
    assert result == 1


def test_count_odds_zero():
    low = 10
    high = 10
    solution = Solution()
    result = solution.countOdds(low, high)
    assert result == 0
