"""

https://en.wikipedia.org/wiki/Bubble_sort

Worst-case performance: O(N^2)

"""

def bubble_sort(array):

    def swap(i, j):
        array[j], array[i] = array[i], array[j]

    swapped = True

    while swapped:
        swapped = False 
        for i in range(len(array) - 1):
            if array[i] > array[i+1]:
                swap(i, i + 1)
                swapped = True

    return array

case1 = [1, 5, 7, 2, 9, 0, 4, 6, 8, 3]

print(bubble_sort(case1))