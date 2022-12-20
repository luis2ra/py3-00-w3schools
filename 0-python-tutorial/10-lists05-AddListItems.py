# @author: https://github.com/luis2ra from https://www.w3schools.com/python/python_lists_add.asp

# Demo Add List Items
'''
Python Lists - Add List Items


Append Items

To add an item to the end of the list, use the append() method:
'''
# Using the append() method to append an item:
list1 = ["apple", "banana", "cherry"]
print('Initial list: ', list1)
list1.append("orange")
print('End list: ', list1)


'''
Insert Items

To insert a list item at a specified index, use the insert() method.

The insert() method inserts an item at the specified index:
'''
# Insert an item as the second position:
list2 = ["apple", "banana", "cherry"]
list2.insert(1, "mango")
print(list2)


'''
Extend List

To append elements from another list to the current list, use the extend() method.
'''
# Add the elements of tropical to fruits:
fruits = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
fruits.extend(tropical)
print(fruits)


'''
Add Any Iterable

The extend() method does not have to append lists, you can add any iterable object (tuples, sets, dictionaries etc.).
'''
# Add elements of a tuple to a list:
thislist = ["apple", "banana", "cherry"]
thistuple = ("kiwi", "orange")
thislist.extend(thistuple)
print(thislist)


# Add elements of a dictionary to a list (review):
fruits_list = ["apple", "banana", "cherry"]
this_dictionary = { "fruit1": "uva", "fruit2": "pear", "fruit3": "kiwi"}
fruits_list.extend(this_dictionary)  # keys added to the list
print(fruits_list)
