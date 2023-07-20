# @author: https://github.com/luis2ra from https://www.w3schools.com/python/numpy/numpy_array_iterating.asp

'''
NumPy Array Iterating


Iterating 2-D Arrays

'''
import numpy as np


# Iterate on the elements of the following 2-D array:
arr = np.array([[1, 2, 3], [4, 5, 6]])

for x in arr:
    for y in x:
        print(y)

### Note: To return the actual values, the scalars, we have to iterate the arrays in each dimension.
