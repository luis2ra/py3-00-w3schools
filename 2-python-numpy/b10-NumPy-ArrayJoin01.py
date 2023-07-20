# @author: https://github.com/luis2ra from https://www.w3schools.com/python/numpy/numpy_array_join.asp

'''
NumPy Joining Array


Joining NumPy Arrays

Joining means putting contents of two or more arrays in a single array.

In SQL we join tables based on a key, whereas in NumPy we join arrays by axes.

We pass a sequence of arrays that we want to join to the concatenate() function, 
along with the axis. If axis is not explicitly passed, it is taken as 0.

'''
import numpy as np


arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])

arr = np.concatenate((arr1, arr2))  # Join two arrays

print(arr)
