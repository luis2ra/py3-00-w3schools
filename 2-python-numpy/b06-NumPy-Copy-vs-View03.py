# @author: https://github.com/luis2ra from https://www.w3schools.com/python/numpy/numpy_copy_vs_view.asp

'''
NumPy Array Copy vs View


The Difference Between Copy and View

The main difference between a copy and a view of an array is that the copy is a new array, and 
the view is just a view of the original array.

The copy owns the data and any changes made to the copy will not affect original array, and 
any changes made to the original array will not affect the copy.

The view does not own the data and any changes made to the view will affect the original array, and 
any changes made to the original array will affect the view.

'''
import numpy as np


arr = np.array([1, 2, 3, 4, 5])

# VIEW: Make a view, change the view, and display both arrays
x = arr.view()
x[0] = 31

print(f"Original array: \n{arr}")
print(f"View array: \n{x}")
