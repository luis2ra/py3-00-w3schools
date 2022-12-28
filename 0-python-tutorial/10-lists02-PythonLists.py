# @author: https://github.com/luis2ra from https://www.w3schools.com/python/python_lists.asp

# Demo Python Lists
'''
Python Lists - List


Lists are used to store multiple items in a single variable.

Lists are one of 4 built-in data types in Python used to store collections of data, the 
other 3 are Tuple, Set, and Dictionary, all with different qualities and usage.

Lists are created using square brackets.

'''
# Create a List:
thislist = ["apple", "banana", "cherry"]
print(thislist)


'''
List Items

List items are ordered, changeable, and allow duplicate values.
List items are indexed, the first item has index [0], the second item has index [1] etc.


Ordered

When we say that lists are ordered, it means that the items have a defined order, and that order will not change.
If you add new items to a list, the new items will be placed at the end of the list.

Note: There are some list methods that will change the order, but in general: the order of the items will not change.


Changeable

The list is changeable, meaning that we can change, add, and remove items in a list after it has been created.


Allow Duplicates

Since lists are indexed, lists can have items with the same value

'''
# Lists allow duplicate values:
thislist = ["apple", "banana", "cherry", "apple", "cherry"]
print(thislist)


'''
List Length

To determine how many items a list has, use the len() function.
'''
# Print the number of items in the list:
thislist2 = ["apple", "banana", "cherry"]
print(len(thislist2))


'''
List Items - Data Types

List items can be of any data type or a list can contain different data types.
'''
# String, int and boolean data types:
list1 = ["apple", "banana", "cherry"]
list2 = [1, 5, 7, 9, 3]
list3 = [True, False, False]
print(list1)
print(list2)
print(list3)

# A list with strings, integers and boolean values:
list4 = ["abc", 34, True, 40, "male"]
print(list4)


'''
type()

From Python's perspective, lists are defined as objects with the data type 'list':
    <class 'list'>
'''
# What is the data type of a list?
mylist = ["apple", "banana", "cherry"]
print(type(mylist))


'''
The list() Constructor

It is also possible to use the list() constructor when creating a new list.

'''
# Using the list() constructor to make a List:
thislist3 = list(("apple", "banana", "cherry"))
print(thislist3)
