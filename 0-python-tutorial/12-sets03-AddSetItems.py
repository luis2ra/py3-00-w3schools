# @author: https://github.com/luis2ra from https://www.w3schools.com/python/python_sets_add.asp

# Demo Add Set Items
'''
Python Sets - Add Set Items


Add Items

Once a set is created, you cannot change its items, but you can add new items.

To add one item to a set use the add() method.
'''
# Add an item to a set, using the add() method:
thisset1 = {"apple", "banana", "cherry"}
thisset1.add("orange")
print(thisset1)


'''
Add Sets

To add items from another set into the current set, use the update() method.
'''
# Add elements from tropical into thisset:
thisset2 = {"apple", "banana", "cherry"}
tropical = {"pineapple", "mango", "papaya"}

thisset2.update(tropical)

print(thisset2)


'''
Add Any Iterable

The object in the update() method does not have to be a set, it can be any iterable object (tuples, lists, dictionaries etc.).
'''
# Add elements of a list to at set:
thisset3 = {"apple", "banana", "cherry"}
mylist = ["kiwi", "orange"]

thisset3.update(mylist)

print(thisset3)
