'''
Given a sorted array nums, remove the duplicates in-place such that 
each element appear only once and return the new length.

Do not allocate extra space for another array, you must do this by 
modifying the input array in-place with O(1) extra memory.

'''

def removeDuplicates(nums):
    for i in nums:
        for j in range(1, nums.count(i)):
            nums.remove(i)
    return len(nums)