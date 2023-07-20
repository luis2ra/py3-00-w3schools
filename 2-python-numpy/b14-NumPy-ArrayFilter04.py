# @author: https://github.com/luis2ra from https://www.w3schools.com/python/numpy/numpy_array_filter.asp

'''
NumPy Filter Array


Creating Filter Directly From Array


In this example, create a filter array that will return only even elements from the original array.

'''
import numpy as np


arr = np.array([1, 2, 3, 4, 5, 6, 7])

filter_arr = arr % 2 == 0

newarr = arr[filter_arr]

print(filter_arr)
print(newarr)
