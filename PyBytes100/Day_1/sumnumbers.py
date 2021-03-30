"""
Write a function that can sum up numbers:

It should receive a sequence of n numbers.
If no argument is provided, return sum of numbers 1..100.
Look closely to the type of the function's default argument ...
Have fun!
"""


def sum_numbers(numbers=None):
    if numbers is None:
        return sum_numbers(range(1,101))
    else:
        result = 0
        for num in numbers:
            result += num
        return result
