'''
NumPy Array Indexing


Negative Indexing

* Use negative indexing to access an array from the end.
'''
import numpy as np

arr = np.array([[1,2,3,4,5], [6,7,8,9,10]])

# Print the last element from the 2nd dim:
print('Last element from 2nd dim: ', arr[1, -1])

