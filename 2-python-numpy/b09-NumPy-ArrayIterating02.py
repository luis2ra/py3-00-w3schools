# @author: https://github.com/luis2ra from https://www.w3schools.com/python/numpy/numpy_array_iterating.asp

'''
NumPy Array Iterating


Iterating 2-D Arrays

'''
import numpy as np


# Iterate on the elements of the following 2-D array:
arr = np.array([[1, 2, 3], [4, 5, 6]])

for x in arr:
    print(x)

### Note: If we iterate on a n-D array it will go through n-1th dimension one by one.
