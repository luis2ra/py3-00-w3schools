# @author: https://github.com/luis2ra from https://www.w3schools.com/python/numpy/numpy_data_types.asp

'''
NumPy Data Types


Creating Arrays With a Defined Data Type

We use the array() function to create arrays, this function can take an optional 
argument dtype that allows us to define the expected data type of the array elements.

'''
import numpy as np



arr1 = np.array([1, 2, 3, 4], dtype='S')    # Create an array with data type string
arr2 = np.array([1, 2, 3, 4], dtype='i4')   # Create an array with data type 4 bytes integer


print(arr1)
print(arr1.dtype)

print()

print(arr2)
print(arr2.dtype)
