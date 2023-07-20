# @author: https://github.com/luis2ra from https://www.w3schools.com/python/numpy/numpy_copy_vs_view.asp

'''
NumPy Array Copy vs View


Check if Array Owns its Data

As mentioned above, copies owns the data, and views does not own the data, but how can we check this?

Every NumPy array has the attribute base that returns None if the array owns the data.

Otherwise, the base  attribute refers to the original object.

'''
import numpy as np


arr = np.array([1, 2, 3, 4, 5])

# Print the value of the base attribute to check if an array owns it's data or not:
x = arr.copy()
y = arr.view()

print(f"checking base attribute for x: \n{x.base}")   # The copy returns None.
print(f"checking base attribute for y: \n{y.base}")   # The view returns the original array.
