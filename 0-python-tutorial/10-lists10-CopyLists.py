# Demo Copy Lists
'''
Copy a List

You cannot copy a list simply by typing list2 = list1, because: list2 will only be a reference to list1, and changes made in list1 will automatically also be made in list2.

There are ways to make a copy, one way is to use the built-in List method copy().

Another way to make a copy is to use the built-in method list().

'''

# Make a copy of a list with the copy() method:
thislist = ["apple", "banana", "cherry"]
mylist = thislist.copy()
print(mylist)


# Make a copy of a list with the list() method:
otherlist = ["yellow", "blue", "red", "green", "gray", "brown"]
mylist = list(otherlist)
print(otherlist)


# Testing use of list2 = list1
list1 = ["a", "b", "c"]
print('valor inicial de list1: ', list1) 
list2 = list1
print('valor inicial de list2: ', list2)
list1.append("d")
print('modificación de list1: ', list1)
print('comprobando que list2 también se modifica: ', list2)
print('En conclusión, el operador = no sirve para hacer una copia de listas')