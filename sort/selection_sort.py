"""
selection sort
"""

def selection_sort(array):
    for i in range(len(array) - 1):
        minimum_idx = i
        for j in range(i+1, len(array)):
            if array[j] < array[minimum_idx]:
                minimum_idx = j
        array[minimum_idx], array[i] = array[i], array[minimum_idx]
    return array

case1 = [1, 5, 7, 2, 9, 0, 4, 6, 8, 3]
print(selection_sort(case1))