# @author: https://github.com/luis2ra from https://www.w3schools.com/python/numpy/numpy_array_search.asp

'''
NumPy Searching Arrays


Searching Arrays

You can search an array for a certain value, and return the indexes that get a match.

To search an array, use the where() method.

'''
import numpy as np


arr = np.array([1, 2, 3, 4, 5, 4, 4])

x = np.where(arr == 4)

print(x)


arr2 = np.array([1, 2, 3, 4, 5, 6, 7, 8])

even = np.where(arr2 % 2 == 0)
odd = np.where(arr2 % 2 == 1)

print(even)
print(odd)
