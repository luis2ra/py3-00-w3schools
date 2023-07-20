# @author: https://github.com/luis2ra from https://www.w3schools.com/python/numpy/numpy_data_types.asp

'''
NumPy Data Types


Data Types in Python

By default Python have these data types:

strings     - used to represent text data, the text is given under quote marks. e.g. "ABCD"
integer     - used to represent integer numbers. e.g. -1, -2, -3
float       - used to represent real numbers. e.g. 1.2, 42.42
boolean     - used to represent True or False.
complex     - used to represent complex numbers. e.g. 1.0 + 2.0j, 1.5 + 2.5j


Data Types in NumPy

NumPy has some extra data types, and refer to data types with one character,
like i for integers, u for unsigned integers etc.

Below is a list of all data types in NumPy and the characters used to represent them.

i - integer
b - boolean
u - unsigned integer
f - float
c - complex float
m - timedelta
M - datetime
O - object
S - string
U - unicode string
V - fixed chunk of memory for other type ( void )


Checking the Data Type of an Array

The NumPy array object has a property called dtype that returns the data type of the array.

'''
import numpy as np


arr1 = np.array([1, 2, 3, 4])
arr2 = np.array(['apple', 'banana', 'cherry'])

# Get the data type of an array object:
print(arr1.dtype)

# Get the data type of an array containing strings:
print(arr2.dtype)
