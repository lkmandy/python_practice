"""
Implement quick sort in Python. Input a list. Output a sorted list.
"""


def partition(array, low, high):
    pivot = array[high]
    i = low - 1

    for j in range(low, high):
        if array[j] <= pivot:
            i = i + 1
            (array[i], array[j]) = (array[j], array[i])
    (array[i + 1], array[high]) = (array[high], array[i + 1])

    return i + 1


def quickSort(array, low, high):
    if low < high:
        pi = partition(array, low, high)
        quickSort(array, low, pi - 1)
        quickSort(array, pi + 1, high)


def initialize_quick_sort(arr):
    quickSort(arr, 0, len(arr) - 1)


test = [21, 4, 1, 3, 9, 20, 25, 6, 21, 14]
initialize_quick_sort(test)

print(test)
