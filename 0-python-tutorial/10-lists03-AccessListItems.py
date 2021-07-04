# Demo Access List Items
'''
List

A list is a collection which is ordered and changeable. In Python lists are written with square brackets.


Access Items

You access the list items by referring to the index number.


Negative Indexing

Negative indexing means beginning from the end, -1 refers to the last item, -2 refers to the second last item etc.


Range of Indexes

You can specify a range of indexes by specifying where to start and where to end the range.
When specifying a range, the return value will be a new list with the specified items.

Note: The search will start at index 2 (included) and end at index 5 (not included).
Remember that the first item has index 0.


Range of Negative Indexes

Specify negative indexes if you want to start the search from the end of the list.

'''

# Print the second item of the list:
thislist = ["apple", "banana", "cherry"]
print(thislist[1])

# Print the last item of the list:
print(thislist[-1])

# Return the third, fourth, and fifth item:
otherlist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(otherlist[2:5])
# Remember that the first item is position 0
# and note that the item in position 5 is NOT included

# This example returns the items from the beginning to "orange":
print(otherlist[:4])

# This example returns the items from "cherry" and to the end:
print(otherlist[2:])

# This example returns the items from index -4 (included) to index -1 (excluded)
print(otherlist[-4:-1])
