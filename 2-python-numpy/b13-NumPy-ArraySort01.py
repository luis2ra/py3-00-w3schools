# @author: https://github.com/luis2ra from https://www.w3schools.com/python/numpy/numpy_array_sort.asp

'''
NumPy Sorting Arrays


Sorting Arrays

Sorting means putting elements in an ordered sequence.

Ordered sequence is any sequence that has an order corresponding to elements, like numeric or alphabetical, 
ascending or descending.

The NumPy ndarray object has a function called sort(), that will sort a specified array.

'''
import numpy as np


# number array
arr = np.array([3, 2, 0, 1])

# string array
arr2 = np.array(['banana', 'cherry', 'apple'])

# boolean array
arr3 = np.array([True, False, True])


print(f"Original array: {arr}")
print(f"Sorted array: {np.sort(arr)}")

print()

print(f"Original array: {arr2}")
print(f"Sorted array: {np.sort(arr2)}")

print()

print(f"Original array: {arr3}")
print(f"Sorted array: {np.sort(arr3)}")
