# @author: https://github.com/luis2ra from https://www.w3schools.com/python/numpy/numpy_array_split.asp

'''
NumPy Splitting Array


Splitting NumPy Arrays

Splitting is reverse operation of Joining.

Joining merges multiple arrays into one and Splitting breaks one array into multiple.

We use array_split() for splitting arrays, we pass it the array we want to split and the number of splits.

If the array has less elements than required, it will adjust from the end accordingly.

'''
import numpy as np


arr = np.array([1, 2, 3, 4, 5, 6])

newarr = np.array_split(arr, 4)

print(newarr)

### Note: We also have the method split() available but it will not adjust the elements 
### when elements are less in source array for splitting like in example above, a
### array_split() worked properly but split() would fail.
