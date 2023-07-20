# @author: https://github.com/luis2ra from https://www.w3schools.com/python/numpy/numpy_array_reshape.asp

'''
NumPy Array Reshaping


Reshaping arrays

Reshaping means changing the shape of an array.

The shape of an array is the number of elements in each dimension.

By reshaping we can add or remove dimensions or change number of elements in each dimension.

'''
import numpy as np


### Reshape From 1-D to 3-D

# 1-D array with 12 elements
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])

# Convert the following 1-D array with 12 elements into a 3-D array
newarr = arr.reshape(2, 3, 2)

print(f"1-D array with 12 elements: \n{arr}")
print()
print(f"Print the shape of a 3-D array: \n{newarr}")
