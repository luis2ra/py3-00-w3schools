'''
NumPy Array Indexing


Access 2-D Arrays

* To access elements from 2-D arrays we can use comma separated integers representing the dimension and the index of the element.

'''
import numpy as np

arr = np.array([[1,2,3,4,5], [6,7,8,9,10]])

# Access the 2nd element on 1st dim:
print('2nd element on 1st dim: ', arr[0, 1])

# Access the 5th element on 2nd dim:
print('5th element on 2nd dim: ', arr[1, 4])

