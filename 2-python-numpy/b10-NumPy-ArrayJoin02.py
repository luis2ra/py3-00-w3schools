# @author: https://github.com/luis2ra from https://www.w3schools.com/python/numpy/numpy_array_join.asp

'''
NumPy Joining Array


Join 2-D Arrays

'''
import numpy as np


arr1 = np.array([[1, 2], [3, 4]])
arr2 = np.array([[5, 6], [7, 8]])

arr = np.concatenate((arr1, arr2), axis=1)  # Join two 2-D arrays along rows (axis=1)

print(arr)
