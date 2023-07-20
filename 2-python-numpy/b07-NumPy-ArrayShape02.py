# @author: https://github.com/luis2ra from https://www.w3schools.com/python/numpy/numpy_array_shape.asp

'''
NumPy Array Shape


Shape of an Array

The shape of an array is the number of elements in each dimension.


Get the Shape of an Array

NumPy arrays have an attribute called shape that returns a tuple with each index having the 
number of corresponding elements.


What does the shape tuple represent?

Integers at every index tells about the number of elements the corresponding dimension has.

In the example above at index-4 we have value 4, so we can say that 5th ( 4 + 1 th) dimension has 4 elements.

'''
import numpy as np


arr = np.array([1, 2, 3, 4], ndmin=5)

print(f"Create an array with 5 dimensions using ndmin: \n{arr}")
print()
print(f"Print the shape of a 5-D array: \n{arr.shape}")
