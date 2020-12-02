# Demo Python Sets
'''
Remove Item

To remove an item in a set, use the remove(), or the discard() method.
Note: If the item to remove does not exist, remove() will raise an error.


You can also use the pop(), method to remove an item, but this method will remove the last item. Remember that sets are unordered, so you will not know what item that gets removed.
The return value of the pop() method is the removed item.
Note: Sets are unordered, so when using the pop() method, you will not know which item that gets removed.


'''

# Remove "banana" by using the remove() method:
thisset = {"apple", "banana", "cherry"}
print("set: ", thisset)
thisset.remove("banana")
print("usando el método <<remove>>: ", thisset)


# Remove "banana" by using the discard() method:
thisset2 = {"apple", "banana", "cherry"}
print("\nset: ", thisset2)
thisset2.discard("banana")
print("usando el método <<discard>>: ", thisset2)


# Note: If the item to remove does not exist, discard() will NOT raise an error.
thisset3 = {"apple", "orange", "cherry"}
print("\nset: ", thisset3)
thisset3.discard("banana")
print("usando el método <<discard>>: ", thisset3)


# Remove the last item by using the pop() method:
thisset4 = {"apple", "banana", "cherry"}
print("\nset: ", thisset4)
x = thisset4.pop()
print("usando el método <<pop>>: ", x)
print(thisset4)


# The clear() method empties the set:
thisset5 = {"apple", "banana", "cherry"}
print("\nset: ", thisset5)
thisset5.clear()
print("usando el método <<clear>>: ", thisset5) 


# The del keyword will delete the set completely:
thisset6 = {"apple", "banana", "cherry"}
print("\nset: ", thisset6)
del thisset6
print("usando el método <<del>>: ", thisset6) 