# @author: https://github.com/luis2ra from https://www.w3schools.com/python/python_sets_remove.asp

# Demo Remove Set Items
'''
Python Sets - Remove Set Items


Remove Item

To remove an item in a set, use the remove(), or the discard() method.

'''
# Remove "banana" by using the remove() method:
thisset1 = {"apple", "banana", "cherry"}
print("set: ", thisset1)
thisset1.remove("banana")  # Note: If the item to remove does not exist, remove() will raise an error.
print("usando el método <<remove>>: ", thisset1)

# Remove "banana" by using the discard() method:
thisset2 = {"apple", "banana", "cherry"}
print("\nset: ", thisset2)
thisset2.discard("banana")  # Note: If the item to remove does not exist, discard() will NOT raise an error.
print("usando el método <<discard>>: ", thisset2)


'''

You can also use the pop(), method to remove an item, but this method will remove the last item.
Remember that sets are unordered, so you will not know what item that gets removed.

The return value of the pop() method is the removed item.

'''
# Remove the last item by using the pop() method:
thisset3 = {"apple", "banana", "cherry"}
print("\nset: ", thisset3)
x = thisset3.pop()  # Note: Sets are unordered, so when using the pop() method, you will not know which item that gets removed.
print("usando el método <<pop>>: ", x)
print(thisset3)


# The clear() method empties the set:
thisset5 = {"apple", "banana", "cherry"}
print("\nset: ", thisset5)
thisset5.clear()
print("usando el método <<clear>>: ", thisset5) 


# The del keyword will delete the set completely:
thisset6 = {"apple", "banana", "cherry"}
print("\nset: ", thisset6)
del thisset6
print("usando el método <<del>>: ", thisset6)  # this will raise an error because the set no exists
