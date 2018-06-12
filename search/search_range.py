"""
Given an array of integers nums sorted in ascending order, find the starting
and ending position of a given target value. If the target is not found in the
array, return [-1, -1].

For example:
Input: nums = [5,7,7,8,8,8,10], target = 8
Output: [3,5]
Input: nums = [5,7,7,8,8,8,10], target = 11
Output: [-1,-1]
"""

def search_range(nums, target):
    # find the first index of target appearing.
    lo, hi = 0, len(nums) - 1
    while lo <= hi:
        mid = (lo + hi) // 2 
        if nums[mid] < target:
            lo = mid + 1 
        elif nums[mid] > target:
            hi = mid - 1
        else:
            break
    
    # find the last index of target appearing 
    for idx in range(len(nums) - 1, mid-1, -1):
        if nums[idx] == target:
            return [mid, idx]

    return [-1, 1]

nums =  [5,7,7,8,8,8,10]
target = 7
print(search_range(nums, target))