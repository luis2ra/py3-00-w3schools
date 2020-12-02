'''
NumPy Array Indexing


Access Array Elements

* Array indexing is the same as accessing an array element.
* You can access an array element by referring to its index number.
* The indexes in NumPy arrays start with 0, meaning that the first element has index 0, and the second has index 1 etc.

'''
import numpy as np

arr = np.array([1, 2, 3, 4])

# Get the first element from the following array:
print(arr[0])

# Get the second element from the following array.
print(arr[1])

# Get third and fourth elements from the following array and add them.
print(arr[2] + arr[3])
