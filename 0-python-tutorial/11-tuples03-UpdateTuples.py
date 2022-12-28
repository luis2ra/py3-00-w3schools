# @author: https://github.com/luis2ra from https://www.w3schools.com/python/python_tuples_update.asp
 
# Demo Update Tuples
'''
Python Tuples - Update Tuples


Tuples are unchangeable, meaning that you cannot change, add, or remove items once the tuple is created.

But there are some workarounds.


Change Tuple Values

You can convert the tuple into a list, change the list, and convert the list back into a tuple.

'''
# Convert the tuple into a list to be able to change it:
x = ("apple", "banana", "cherry")
y = list(x)
y[1] = "kiwi"
x = tuple(y)

print(x)


'''

Add Items

Since tuples are immutable, they do not have a build-in append() method, but there are other ways to add items to a tuple.

1. Convert into a list: 
Just like the workaround for changing a tuple, you can convert it into a list, add your item(s), and convert it back into a tuple.

'''
# Convert the tuple into a list, add "orange", and convert it back into a tuple:
thistuple1 = ("apple", "banana", "cherry")
y1 = list(thistuple1)
y1.append("orange")
thistuple1 = tuple(y1)
print(thistuple1)

'''

2. Add tuple to a tuple.
You are allowed to add tuples to tuples, so if you want to add one item, (or many), create a new tuple with the item(s), and add it to the existing tuple:

'''
# Create a new tuple with the value "orange", and add that tuple:
thistuple2 = ("apple", "banana", "cherry")
y2 = ("orange",)
thistuple2 += y2
print(thistuple2)


'''

Remove Items

Note: You cannot remove items in a tuple.

Tuples are unchangeable, so you cannot remove items from it, but you can use the same workaround as we used for changing and adding tuple items:

'''
# Convert the tuple into a list, remove "apple", and convert it back into a tuple:
thistuple3 = ("apple", "banana", "cherry")
y3 = list(thistuple3)
y3.remove("apple")
thistuple3 = tuple(y3)
print(thistuple3)


'''

Delete Tuple

You can delete the tuple completely:

'''
# The del keyword can delete the tuple completely:
thistuple = ("apple", "banana", "cherry")
del thistuple
print(thistuple)  # this will raise an error because the tuple no longer exists
