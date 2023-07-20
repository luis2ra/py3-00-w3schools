# @author: https://github.com/luis2ra from https://www.w3schools.com/python/numpy/numpy_array_search.asp

'''
NumPy Searching Arrays


Search Sorted

There is a method called searchsorted() which performs a binary search in the array, and returns 
the index where the specified value would be inserted to maintain the search order.

The searchsorted() method is assumed to be used on sorted arrays.

'''
import numpy as np


arr = np.array([6, 7, 8, 9])

# Find the indexes where the value 7 should be inserted
x = np.searchsorted(arr, 7)

print(x)  # The number 7 should be inserted on index 1 to remain the sort order.
