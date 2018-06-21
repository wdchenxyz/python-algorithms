"""
Given an array of integers that is already sorted in ascending order, find two
numbers such that they add up to a specific target number. The function two_sum
should return indices of the two numbers such that they add up to the target,
where index1 must be less than index2. Please note that your returned answers
(both index1 and index2) are not zero-based.
You may assume that each input would have exactly one solution and you
may not use the same element twice.

Input: numbers = [2, 7, 11, 15], target=9
Output: index1 = 1, index2 = 2

Solution:
two_sum: using binary search
two_sum1: using dictionary as a hash table
two_sum2: using two pointers
"""

def two_sum(nums, target):
    for i in range(len(nums)):
        second = target - nums[i]
        # find whether second exists
        lo = i + 1
        hi = len(nums) - 1
        while lo <= hi:
            mid = (lo + hi) // 2
            if second == nums[mid]:
                return [i, mid]
            elif nums[mid] > target:
                hi = mid - 1
            else:
                lo = mid + 1
    return -1 # if no such pair exists

import collections
def two_sum1(nums, target):
    dictionary = collections.defaultdict(int)
    for idx, num in enumerate(nums):
        if num in dictionary:
            return [dictionary[num], idx]
        dictionary[target - num] = idx
    return -1 # if no such pair exists

# works under 'ascending' constraint
def two_sum2(nums, target):
    p1 = 0
    p2 = len(nums) - 1
    while p1 <= p2:
        s = nums[p1] + nums[p2]
        if s == target:
            return [p1, p2]
        elif target > s:
            p1 += 1
        else:
            p2 -= 1
    return -1
            

case1 = [2, 7, 11, 15] 
target = 17
print(two_sum(case1, target))
print(two_sum1(case1, target))
print(two_sum2(case1, target))