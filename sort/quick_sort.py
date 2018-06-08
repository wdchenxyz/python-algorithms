"""
quick sort
"""

def partition(array, front, end):
    pivot = array[end]
    wall = front
    for position in range(front, end):
        if array[position] < pivot:
            array[position], array[wall] = array[wall], array[position]
            wall += 1
    array[wall], array[end] = pivot, array[wall]
    return wall

def quick_sort(array, front, end):

    if end > front:
        pivot = partition(array, front, end)
        quick_sort(array, front, pivot - 1)
        quick_sort(array, pivot + 1, end)
    
    return array

case1 = [1, 5, 7, 2, 9, 0, 4, 6, 8, 3]
print(quick_sort(case1, 0, len(case1) - 1 ))