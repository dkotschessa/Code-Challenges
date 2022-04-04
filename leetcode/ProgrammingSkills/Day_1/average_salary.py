"""You are given an array of unique integers salary
 where salary[i] is the salary of the ith employee.

Return the average salary of employees
 excluding the minimum and maximum salary.
  Answers within 10-5 of the actual answer will be accepted.
"""
from typing import List
from statistics import mean


class Solution:
    def average(self, salary: List[int]) -> float:
        average = mean(sorted(salary)[1:-1])
        return float(average)
