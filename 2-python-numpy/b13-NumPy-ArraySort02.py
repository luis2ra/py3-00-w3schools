# @author: https://github.com/luis2ra from https://www.w3schools.com/python/numpy/numpy_array_sort.asp

'''
NumPy Sorting Arrays


Sorting a 2-D Array

If you use the sort() method on a 2-D array, both arrays will be sorted.

'''
import numpy as np


# Sort a 2-D array
arr = np.array([[3, 2, 4], [5, 0, 1]])

print(f"Original array: \n{arr}")
print(f"Sorted array: \n{np.sort(arr)}")
