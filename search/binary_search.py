"""
# Binary search works for a sorted array.
# Note: The code logic is written for an array sorted in
#       increasing order.
# T(n): O(log n)
"""

def binary_search(array, query):
    lo, hi = 0, len(array) - 1
    while lo <= hi:
        mid = (lo + hi) // 2
        if array[mid] == query:
            return mid
        if array[mid] < query:
            lo = mid + 1
        else :
            hi = mid - 1
    
    return None

case1 = [1, 2, 4, 5, 7, 8, 9]
print(binary_search(case1, 9))