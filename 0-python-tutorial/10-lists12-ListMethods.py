# @author: https://github.com/luis2ra from https://www.w3schools.com/python/python_lists_methods.asp

# Demo List Methods
'''
Python Lists - List Methods


List Methods

Python has a set of built-in methods that you can use on lists.

Method ---- Description

append()	Adds an element at the end of the list
clear()		Removes all the elements from the list
copy()		Returns a copy of the list
count()		Returns the number of elements with the specified value
extend()	Add the elements of a list (or any iterable), to the end of the current list
index()		Returns the index of the first element with the specified value
insert()	Adds an element at the specified position
pop()		Removes the element at the specified position
remove()	Removes the item with the specified value
reverse()	Reverses the order of the list
sort()		Sorts the list

'''
# Example:
strs = ['0', '1', '2']
print([int(x) for x in strs])
print(list(map(int, strs)))
# print(strs.map(lambda x: int(x)))
