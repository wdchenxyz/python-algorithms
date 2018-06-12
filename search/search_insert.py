"""
Given a sorted array and a target value, return the index if the target is
found. If not, return the index where it would be if it were inserted in order.

For example:
[1,3,5,6], 5 -> 2
[1,3,5,6], 2 -> 1
[1,3,5,6], 7 -> 4
[1,3,5,6], 0 -> 0
"""

def search_insert(array, value):
    lo, hi = 0, len(array)-1
    while lo <= hi:
        mid = (lo + hi) // 2
        if value > array[mid]:
            lo = mid + 1
        elif value < array[mid]:
            hi = mid - 1
        else:
            return mid
    return lo

case1 = [1, 3, 5, 6]
target = 4
print(search_insert(case1, target))