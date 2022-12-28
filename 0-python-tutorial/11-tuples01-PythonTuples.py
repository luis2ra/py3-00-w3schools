# @author: https://github.com/luis2ra from https://www.w3schools.com/python/python_tuples.asp

# Demo Python Tuples
'''
Python Tuples - Tuples


Tuple

Tuples are used to store multiple items in a single variable.

Tuple is one of 4 built-in data types in Python used to store collections of data, the 
other 3 are List, Set, and Dictionary, all with different qualities and usage.

A tuple is a collection which is ordered and unchangeable.

Tuples are written with round brackets.

'''
# Create a Tuple:
thistuple = ("apple", "banana", "cherry")
print(thistuple)


'''
Tuple Items

Tuple items are ordered, unchangeable, and allow duplicate values.

Tuple items are indexed, the first item has index [0], the second item has index [1] etc.


Ordered

When we say that tuples are ordered, it means that the items have a defined order, and that order will not change.


Unchangeable

Tuples are unchangeable, meaning that we cannot change, add or remove items after the tuple has been created.


Allow Duplicates

Since tuples are indexed, they can have items with the same value:

'''
# Tuples allow duplicate values:
thistuple2 = ("apple", "banana", "cherry", "apple", "cherry")
print(thistuple2)


'''
Tuple Length

To determine how many items a tuple has, use the len() function:

'''
# Print the number of items in the tuple:
thistuple3 = ("apple", "banana", "cherry")
print(len(thistuple3))


'''
Create Tuple With One Item

To create a tuple with only one item, you have to add a comma after the item, otherwise Python will not recognize it as a tuple.

'''
# One item tuple, remember the comma:
thistuple4 = ("apple",)
print(type(thistuple4))

#NOT a tuple
thistuple5 = ("apple")
print(type(thistuple5))


'''
Tuple Items - Data Types

Tuple items can be of any data type:

'''
# String, int and boolean data types:
tuple1 = ("apple", "banana", "cherry")
tuple2 = (1, 5, 7, 9, 3)
tuple3 = (True, False, False)
print(tuple1)
print(tuple2)
print(tuple3)

# A tuple can contain different data types:
tuple4 = ("abc", 34, True, 40, "male")
print(tuple4)


'''
type()

From Python's perspective, tuples are defined as objects with the data type 'tuple':

<class 'tuple'>

'''
# What is the data type of a tuple?
mytuple = ("apple", "banana", "cherry")
print(type(mytuple))


'''
The tuple() Constructor

It is also possible to use the tuple() constructor to make a tuple.

'''
# Using the tuple() method to make a tuple:
thistuple = tuple(("apple", "banana", "cherry"))  # note the double round-brackets
print(thistuple)
