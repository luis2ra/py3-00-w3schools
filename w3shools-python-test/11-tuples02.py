# Demo Python Tuples
'''
Access Tuple Items

You can access tuple items by referring to the index number, inside square brackets.


Negative Indexing
Negative indexing means beginning from the end, -1 refers to the last item, -2 refers to the second last item etc.


Range of Indexes
You can specify a range of indexes by specifying where to start and where to end the range.
When specifying a range, the return value will be a new tuple with the specified items.


Range of Negative Indexes
Specify negative indexes if you want to start the search from the end of the tuple.

'''

# Print the second item in the tuple:
thistuple = ("apple", "banana", "cherry")
print(thistuple[1])


# Negative Indexing
# Print the last item of the tuple:
thistuple = ("apple", "banana", "cherry")
print(thistuple[-1])


# Range of Indexes
# Return the third, fourth, and fifth item:
thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[2:5])       # Note: The search will start at index 2 (included) and end at index 5 (not included).


# Range of Negative Indexes
# This example returns the items from index -4 (included) to index -1 (excluded)
thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[-4:-1])