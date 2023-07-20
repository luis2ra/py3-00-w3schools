# @author: https://github.com/luis2ra from https://www.w3schools.com/python/numpy/numpy_array_iterating.asp

'''
NumPy Array Iterating


Iterating Arrays

Iterating means going through elements one by one.

As we deal with multi-dimensional arrays in numpy, we can do this using basic for loop of python.

If we iterate on a 1-D array it will go through each element one by one.

'''
import numpy as np


### Iterating 1-D Arrays

# Iterate on the elements of the following 1-D array:
arr = np.array([1, 2, 3])

for x in arr:
    print(x)
