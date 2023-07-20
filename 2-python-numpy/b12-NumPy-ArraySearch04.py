# @author: https://github.com/luis2ra from https://www.w3schools.com/python/numpy/numpy_array_search.asp

'''
NumPy Searching Arrays


Multiple Values

To search for more than one value, use an array with the specified values.

'''
import numpy as np


arr = np.array([1, 3, 5, 7])

# Find the indexes where the values 2, 4, and 6 should be inserted:
x = np.searchsorted(arr, [2, 4, 6])

print(x)  # The return value is: [1 2 3] containing the three indexes where 2, 4, 6 would be inserted in the original array to maintain the order.
