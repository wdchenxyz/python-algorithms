"""
# Find first occurance of a number in a sorted array (increasing order)
# Approach- Binary Search
# T(n): O(log n)
"""

def first_occurance(nums, target):
    lo, hi = 0, len(nums) - 1
    while lo <= hi:
        mid = (lo + hi) // 2
        if ((mid == 0) or (target > nums[mid-1])) and (nums[mid] == target):
            return mid
        elif nums[mid] < target:
            lo = mid + 1 
        else:
            hi = mid - 1
    return -1

def last_occurance(nums, target):
    lo, hi = 0, len(nums) - 1
    while lo <= hi:
        mid = (lo + hi) // 2
        if ((mid == len(nums) - 1) or (target < nums[mid+1])) and (nums[mid] == target):
            return mid
        elif nums[mid] > target:
            hi = mid - 1
        else:
            lo = mid + 1
    return -1

case1 = [1, 2, 4, 5, 5, 5, 5, 5, 7, 7, 9]
print(first_occurance(case1, 5))
print(last_occurance(case1, 5))