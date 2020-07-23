# Demo Python Sets
'''
Change Items

Once a set is created, you cannot change its items, but you can add new items.


Add Items

To add one item to a set use the add() method.

To add more than one item to a set use the update() method.

'''

# Add an item to a set, using the add() method:
thisset = {"apple", "banana", "cherry"}
thisset.add("orange")
print(thisset)


# Add multiple items to a set, using the update() method:
thisset_other = {"apple", "banana", "cherry"}
thisset_other.update(["orange", "mango", "grapes"])
print(thisset_other) 