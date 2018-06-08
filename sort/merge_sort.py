"""
merge sort
"""

def merge(left, right, merged):
    left_cursor, right_cursor = 0, 0
    while left_cursor < len(left) and right_cursor < len(right):
        if left[left_cursor] < right[right_cursor] :
            merged[left_cursor + right_cursor] = left[left_cursor]
            left_cursor += 1
        else:
            merged[left_cursor + right_cursor] = right[right_cursor]
            right_cursor += 1
        
    # merge rest results into merged
    for left_cursor in range(left_cursor, len(left)):
        merged[left_cursor + right_cursor] = left[left_cursor]
    for right_cursor in range(right_cursor, len(right)):
        merged[left_cursor + right_cursor] = right[right_cursor]
    return merged

def merge_sort(array):
    
    if len(array) <= 1:
        return array
    
    mid = len(array) // 2
    left = merge_sort(array[:mid])
    right = merge_sort(array[mid:])
    
    merged = merge(left, right, array[:])
    return merged

case1 = [1, 5, 7, 2, 9, 0, 4, 6, 8, 3]
print(merge_sort(case1))