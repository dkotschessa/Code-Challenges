"""
Given an array of integers nums.

A pair (i,j) is called good if nums[i] == nums[j] and i < j (INDEX)

Return the number of good pairs.

 

Example 1:

Input: nums = [1,2,3,1,1,3]
Output: 4
Explanation: There are 4 good pairs (0,3), (0,4), (3,4), (2,5) 0-indexed.
Example 2:

Input: nums = [1,1,1,1]
Output: 6
Explanation: Each pair in the array are good.
Example 3:

Input: nums = [1,2,3]
Output: 0
"""



def Pairs(nums):
    # return all pairs in an array
    # regardless of weather they match
    pairs = []
    for i in nums:
        for j in nums:
            if nums.index(i) != nums.index(j):
                pairs.append((i,j))

            
    
    return pairs


# def goodPairs(nums):
#     pairs = []
#     for i in nums:
#         occurences = nums.count(i)
#         num_index = nums.index(i)
#         if occurences > 1:
#             for _ in range(occurences):
#                 nums[num_index] = 'x'
#                 pairs.append((num_index, nums.index(i)))           
#     return pairs


def goodPairs(nums):
    pairs = []
    for i in nums:
        num_index = nums.index(i)
        nums_without_i = nums[num_index:]
        if i in nums_without_i:
            next_index = nums.index(i, num_index)
            pair = (num_index, next_index)
            pairs.append(pair)
    return pairs


