"""
# Find first occurance of a number in a sorted array (increasing order)
# Approach- Binary Search
# T(n): O(log n)
"""

def first_occurance(nums, target):
    lo, hi = 0, len(nums) - 1
    while lo < hi:
        mid = (lo + hi) // 2
        if nums[mid] < target:
            lo = mid + 1
        else:
            hi = mid
    if (nums[lo] == target):
        return lo
    return -1

case1 = [1, 2, 4, 5, 5, 5, 5, 5, 7, 8, 9]
print(first_occurance(case1, 5))