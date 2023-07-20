# @author: https://github.com/luis2ra from https://www.w3schools.com/python/numpy/numpy_creating_arrays.asp

'''
Create a NumPy ndarray Object

* NumPy is used to work with arrays. The array object in NumPy is called ndarray.
* We can create a NumPy ndarray object by using the array() function.
* To create an ndarray, we can pass a list, tuple or any array-like object into the array() method, 
  and it will be converted into an ndarray

'''
import numpy as np

# Generando un ndarray desde una lista
arr1 = np.array([1, 2, 3, 4, 5])

print(arr1)
print(type(arr1))


# Generando un ndarray desde una tupla
arr2 = np.array((6, 7, 8, 9, 10))
print(arr2)


arr3 = np.array((1, 2, 3, 4, 5))
print(arr3)
