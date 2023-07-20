# @author: https://github.com/luis2ra from https://www.w3schools.com/python/numpy/numpy_array_slicing.asp

'''
NumPy Array Slicing


Slicing 2-D Arrays

'''
import numpy as np


arr = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])

# From the second element, slice elements from index 1 to index 4 (not included):
print(arr[1, 1:4])
print()

# From both elements, return index 2:
print(arr[0:2, 2])
print()

# From both elements, slice index 1 to index 4 (not included), this will return a 2-D array:
print(arr[0:2, 1:4])
