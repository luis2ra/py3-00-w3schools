# @author: https://github.com/luis2ra from https://www.w3schools.com/python/numpy/numpy_array_filter.asp

'''
NumPy Filter Array


Creating Filter Directly From Array

The above example (view b14-NumPy-ArrayFilter02.py) is quite a common task in NumPy and 
NumPy provides a nice way to tackle it.

We can directly substitute the array instead of the iterable variable in our condition and 
it will work just as we expect it to.

'''
import numpy as np


arr = np.array([41, 42, 43, 44])

filter_arr = arr > 42

newarr = arr[filter_arr]

print(filter_arr)
print(newarr)
