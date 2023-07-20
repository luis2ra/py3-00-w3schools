# @author: https://github.com/luis2ra from https://www.w3schools.com/python/numpy/numpy_array_search.asp

'''
NumPy Searching Arrays


Search From the Right Side

By default the left most index is returned, but we can give side='right' to return the right most index instead.

'''
import numpy as np


arr = np.array([6, 7, 8, 9])

# Find the indexes where the value 7 should be inserted, starting from the right:
x = np.searchsorted(arr, 7, side='right')

print(x)  # The number 7 should be inserted on index 2 to remain the sort order.
