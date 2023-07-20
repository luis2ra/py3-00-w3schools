# @author: https://github.com/luis2ra from https://www.w3schools.com/python/numpy/numpy_array_iterating.asp

'''
NumPy Array Iterating


Iterating 3-D Arrays

'''
import numpy as np


# Iterate on the elements of the following 3-D array:
arr = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])

for x in arr:
    for y in x:
        for z in y:
            print(z)

### Note: To return the actual values, the scalars, we have to iterate the arrays in each dimension.
