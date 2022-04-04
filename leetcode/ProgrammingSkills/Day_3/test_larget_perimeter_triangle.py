from largest_perimeter_triangle import Solution

solution = Solution()


def test_largest_area_triangle():
    result = solution.largestPerimeter([2, 1, 2])
    assert result == 5


def test_largest_area_triangle_zero():
    result = solution.largestPerimeter([1, 2, 1])
    assert result == 0


def test_four_length_array():
    result = solution.largestPerimeter([3, 6, 2, 3])
    assert result == 8
