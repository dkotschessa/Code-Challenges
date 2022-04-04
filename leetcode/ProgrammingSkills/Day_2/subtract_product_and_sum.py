"""
Given an integer number n, return the 
difference between the product of its digits and the sum of its digits.
"""


class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        digits = [int(x) for x in str(n)]
        prod = 1
        for x in digits:
            prod *= x
        summation = sum(digits)
        return prod - summation
