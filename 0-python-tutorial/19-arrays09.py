# @author: https://github.com/luis2ra from https://www.w3schools.com/python/python_arrays.asp

# Demo Python Arrays - Array Methods
'''
Array Methods

Python has a set of built-in methods that you can use on lists/arrays.


Method --------	Description

append()	    Adds an element at the end of the list
clear()	        Removes all the elements from the list
copy()	        Returns a copy of the list
count()	        Returns the number of elements with the specified value
extend()	    Add the elements of a list (or any iterable), to the end of the current list
index()	        Returns the index of the first element with the specified value
insert()	    Adds an element at the specified position
pop()	        Removes the element at the specified position
remove()	    Removes the first item with the specified value
reverse()	    Reverses the order of the list
sort()	        Sorts the list


Note: Python does not have built-in support for Arrays, but Python Lists can be used instead.

'''
# Example de copy()
cars = ["Ford", "Volvo", "BMW"]
cars_2 = cars.copy()
print(cars_2)

# Example de clear()
cars.clear()
print(cars)
print(cars_2)

# Example de count()
#contador = count(cars_2)
#print(contador)
