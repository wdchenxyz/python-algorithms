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
    
    return -1

def binary_search_recur(array, low, high, query):
    if low > high:
        return -1
    mid = (low + high) // 2
    if array[mid] < query:
        return binary_search_recur(array, mid+1, high, query)
    elif array[mid] > query:
        return binary_search_recur(array, low, mid-1, query)
    else:
        return mid

case1 = [1, 2, 4, 5, 7, 8, 9]
print(binary_search(case1, 5))
print(binary_search_recur(case1, 0, len(case1)-1, 5))
