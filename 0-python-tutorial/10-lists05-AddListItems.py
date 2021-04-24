# Demo Add List Items
'''
Add Items

To add an item to the end of the list, use the append() method.

To add an item at the specified index, use the insert() method.


Extend List

To append elements from another list to the current list, use the extend() method.


Add Any Iterable

The extend() method does not have to append lists, you can add any iterable object (tuples, sets, dictionaries etc.).

'''

# Using the append() method to append an item:
list1 = ["apple", "banana", "cherry"]
print('Initial list: ', list1)
list1.append("orange")
print('End list: ', list1)


# Insert an item as the second position:
list2 = ["apple", "banana", "cherry"]
list2.insert(1, "mango")
print(list2)


# Add the elements of tropical to fruits:
fruits = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
fruits.extend(tropical)
print(fruits)


# Add elements of a tuple to a list:
thislist = ["apple", "banana", "cherry"]
thistuple = ("kiwi", "orange")
thislist.extend(thistuple)
print(thislist)


# Add elements of a dictionary to a list (review):
fruits_list = ["apple", "banana", "cherry"]
this_dictionary = { "fruit1": "uva", "fruit2": "pear", "fruit3": "kiwi"}
fruits_list.extend(this_dictionary)
print(fruits_list)