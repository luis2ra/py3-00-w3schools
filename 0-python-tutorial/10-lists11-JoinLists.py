# Demo Join Lists
'''
Join Two Lists

There are several ways to join, or concatenate, two or more lists in Python.

One of the easiest ways are by using the + operator.

Another way to join two lists are by appending all the items from list2 into list1, one by one.

Or you can use the extend() method, which purpose is to add elements from one list to another list.

'''

# Join two list:
list1 = ["a", "b", "c"]
print(list1) 
list2 = [1, 2, 3]
print(list2) 
list_join = list1 + list2
print(list_join) 


# Append list4 into list3:
list3 = ["d", "e", "f"]
print(list3) 
list4 = [4, 5, 6]
print(list4) 

for x in list4:
    list3.append(x)
print(list3) 


# Use the extend() method to add list6 at the end of list5:
list5 = ["x", "y", "z"]
print(list5) 
list6 = [7, 8, 9]
print(list6) 

list5.extend(list6)
print(list5) 
