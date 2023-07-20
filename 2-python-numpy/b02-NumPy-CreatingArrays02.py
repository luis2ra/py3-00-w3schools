# @author: https://github.com/luis2ra from https://www.w3schools.com/python/numpy/numpy_creating_arrays.asp

'''
Dimensions in Arrays

* A dimension in arrays is one level of array depth (nested arrays).
* nested array: are arrays that have arrays as their elements.


0-D Arrays

* 0-D arrays, or Scalars, are the elements in an array. Each value in an array is a 0-D array.

1-D Arrays

* An array that has 0-D arrays as its elements is called uni-dimensional or 1-D array.

2-D Arrays

* An array that has 1-D arrays as its elements is called a 2-D array.

3-D Arrays

* An array that has 2-D arrays (matrices) as its elements is called 3-D array.


Check Number of Dimensions?

* NumPy Arrays provides the ndim attribute that returns an integer that tells us how many dimensions the array have.

'''
import numpy as np

# Create a 0-D array with value 42
arr0 = np.array(42)
print(arr0)
print(type(arr0))
print('Dimensión: ', arr0.ndim)
print('\n')

# Create a 1-D array containing the values 1,2,3,4,5:
arr1 = np.array([1, 2, 3, 4, 5])
print(arr1)
print(type(arr1))
print('Dimensión: ', arr1.ndim)
print('\n')


# Create a 2-D array containing two arrays with the values 1,2,3 and 4,5,6:
arr2 = np.array([[1, 2, 3], [4, 5, 6]])
print(arr2)
print(type(arr2))
print('Dimensión: ', arr2.ndim)
print('\n')


# Create a 3-D array with two 2-D arrays, both containing two arrays with the values 1,2,3 and 4,5,6:
arr3 = np.array([ [[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]] ])
print(arr3)
print(type(arr3))
print('Dimensión: ', arr3.ndim)
