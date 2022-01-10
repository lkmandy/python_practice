"""
Implement quick sort in Python. Input a list. Output a sorted list.

"""
import sys 
sys.setrecursionlimit(10**6) 


def quicksort(array):
    if len(array) <=1:
        return array
    
    pivot = array.pop()
    big_nums = []
    small_nums = []
    
    for item in array:
        if item > pivot:
            big_nums.append(item)
        else:
            small_nums.append(item)

    return quicksort(small_nums + [pivot] + big_nums)

test = [21, 4, 1, 3, 9, 20, 25, 6, 21, 14]
print (quicksort(test))

