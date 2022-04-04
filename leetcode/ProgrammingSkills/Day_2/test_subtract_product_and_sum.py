from .subtract_product_and_sum import Solution

solution = Solution()


def test_sub_prod_sum_234():
    n = 234
    result = solution.subtractProductAndSum(n)
    assert result == 15


def test_sub_prod_sum_4421():
    n = 4421
    result = solution.subtractProductAndSum(n)
    assert result == 21
