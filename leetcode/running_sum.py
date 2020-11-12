"""
Given an array nums. We define a running sum of an array as runningSum[i] = sum(nums[0]…nums[i]).

Input: nums = params = [([1,2,3,4], [1,3, 6, 10]),
           ([1,1,1,1,1], [1,2,3,4,5]),
           ([[3,1,2,10,1], [3,4,6,16,17])]

Output: [1,3,6,10]
Explanation: Running sum is obtained as follows: [1, 1+2, 1+2+3, 1+2+3+4].
Example 2:

Input: nums = [1,1,1,1,1]
Output: [1,2,3,4,5]
Explanation: Running sum is obtained as follows: [1, 1+1, 1+1+1, 1+1+1+1, 1+1+1+1+1].
Example 3:

Input: nums = [3,1,2,10,1]
Output: [3,4,6,16,17]
"""

def runningSum(arr): #quick and dirty - how to improve?
    return [sum(arr[0:n]) for n in range(1, len(arr)+ 1)]


def runningSum2(arr):
    return [sum(arr[0:n]) for n,m in enumerate(arr, 1)]

