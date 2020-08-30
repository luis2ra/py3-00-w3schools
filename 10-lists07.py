# Demo Python Lists
'''
List

A list is a collection which is ordered and changeable. In Python lists are written with square brackets.


Add Items

To add an item to the end of the list, use the append() method.

To add an item at the specified index, use the insert() method.

'''

# Using the append() method to append an item:
thislist = ["apple", "banana", "cherry"]
print(thislist)
thislist.append("orange")
print(thislist)


# Insert an item as the second position:
thislist.insert(1, "mango")
print(thislist)