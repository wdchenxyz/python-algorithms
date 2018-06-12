"""
# Find first occurance of a number in a sorted array (increasing order)
# Approach- Binary Search
# T(n): O(log n)
"""

def first_occurance(array, query):
    lo, hi = 0, len(array) - 1
    while lo <= hi:
        mid = (lo + hi) // 2
        if array[mid] == query:
            return mid
        if array[mid] < query:
            lo = mid + 1
        else :
            hi = mid - 1
    
    return -1

case1 = [1, 2, 4, 5, 7, 8, 9]
print(first_occurance(case1, 5))