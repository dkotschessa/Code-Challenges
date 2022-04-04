from .average_salary import Solution


def test_average_salary():
    salary = [4000, 3000, 1000, 2000]
    expected = 2500.00000
    solution = Solution()
    result = solution.average(salary)
    assert result == expected


def test_average_salary_length_three():
    salary = [1000, 2000, 3000]
    expected = 2000.00000
    solution = Solution()
    result = solution.average(salary)
    assert result == expected
