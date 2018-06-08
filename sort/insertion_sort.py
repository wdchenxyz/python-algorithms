"""
insertion sort
"""

def insertion_sort(array):

    for i in range(1, len(array)):
        key = array[i]
        j = i - 1
        while key < array[j] and j >= 0 :
            array[j+1] = array[j]
            j -= 1
        array[j+1] = key
    return array

case1 = [1, 5, 7, 2, 9, 0, 4, 6, 8, 3]
print(insertion_sort(case1))