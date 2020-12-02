'''
Higher Dimensional Arrays

* An array can have any number of dimensions.
* When the array is created, you can define the number of dimensions by using the ndmin argument.

'''
import numpy as np

# Create an array with 5 dimensions and verify that it has 5 dimensions:
arr = np.array([1, 2, 3, 4], ndmin=5)

print(arr)
print('Number of dimensions: ', arr.ndim)

'''
In this array the innermost dimension (5th dim) has 4 elements, 
the 4th dim has 1 element that is the vector, 
the 3rd dim has 1 element that is the matrix with the vector, 
the 2nd dim has 1 element that is 3D array 
and 1st dim has 1 element that is a 4D array.

'''