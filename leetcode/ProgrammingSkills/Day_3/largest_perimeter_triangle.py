"""Given an integer array nums, return the largest perimeter
 of a triangle with a non-zero area, formed from three of these 
 lengths. If it is impossible to form any triangle of a non-zero area,
  return 0."""


from typing import List
from math import sqrt
from itertools import combinations


# class Solution:
#     def largestPerimeter(self, nums: List[int]) -> int:
#         # get all possible 3 combinations
#         triangles = list(combinations(nums, 3))  # may not need list
#         good_triangles = []
#         for sides in triangles:
#             a, b, c = sides
#             s = sum(sides) / 2  # semi perimeter
#             radicand = s * (s - a) * (s - b) * (s - c)
#             try:
#                 herons_formula = sqrt(radicand)
#                 if herons_formula > 0:
#                     good_triangles.append(sides)
#             except ValueError:
#                 return 0
#         if perimeters := [sum(sides) for sides in good_triangles]:
#             return max(perimeters)
#         else:
#             return 0


class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums = sorted(nums)
        c = nums.pop()
        a, b = nums[-2::]

        # find a and b s.t a + b < c

        sides = sorted(nums)[-3::]
        a, b, c = sides
        if a + b > c:
            return a + b + c
        else:
            return 0


solution = Solution()


"""This leads to a simple algorithm: 
Sort the array. For any c in the array, we
choose the largest possible a \leq b \leq ca≤b≤c: 
these are just the two values adjacent to cc. If this 
forms a triangle, we return the answer.
"""

# if __name__ == "__main__":
#     solution.largestPerimeter([3, 6, 2, 3])
