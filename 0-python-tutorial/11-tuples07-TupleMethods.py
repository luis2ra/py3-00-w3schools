# @author: https://github.com/luis2ra from https://www.w3schools.com/python/python_tuples_join.asp

# Demo Tuple Methods
'''
Python Tuples - Tuple Methods


Tuple Methods

Python has two built-in methods that you can use on tuples.

Method	--- Description

count() 	Returns the number of times a specified value occurs in a tuple
index()	    Searches the tuple for a specified value and returns the position of where it was found

'''
# Return the number of times the value 5 appears in the tuple:
thistuple1 = (1, 3, 7, 8, 7, 5, 4, 6, 8, 5)
x = thistuple1.count(5)
print(x)


# Search for the first occurrence of the value 8, and return its position:
thistuple2 = (1, 3, 7, 8, 7, 5, 4, 6, 8, 5)
y = thistuple2.index(8)
print(y)
