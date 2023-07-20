# @author: https://github.com/luis2ra from https://www.w3schools.com/python/numpy/numpy_array_slicing.asp

'''
NumPy Array Slicing


Slicing arrays

Slicing in python means taking elements from one given index to another given index.

We pass slice instead of index like this: [start:end].

We can also define the step, like this: [start:end:step].

If we don't pass start its considered 0

If we don't pass end its considered length of array in that dimension

If we don't pass step its considered 1


Negative Slicing

Use the minus operator to refer to an index from the end.


STEP

Use the step value to determine the step of the slicing.

'''
import numpy as np


# Slice elements from index 1 to index 5 from the following array:
arr = np.array([1, 2, 3, 4, 5, 6, 7])
print(arr[1:5])  # Note: The result includes the start index, but excludes the end index.


# Slice elements from index 4 to the end of the array:
print(arr[4:])  


# Slice elements from the beginning to index 4 (not included):
print(arr[:4])


# Slice from the index 3 from the end to index 1 from the end:
print(arr[-3:-1])


# Return every two step element from index 1 to index 5:
print(arr[1:5:2])


# Return every two step element from the entire array:
print(arr[::2])
