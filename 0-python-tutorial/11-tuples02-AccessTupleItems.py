# @author: https://github.com/luis2ra from https://www.w3schools.com/python/python_tuples_access.asp

# Demo Access Tuple Items
'''
Python Tuples - Access Tuple Items


Access Tuple Items

You can access tuple items by referring to the index number, inside square brackets.

'''
# Print the second item in the tuple:
thistuple1 = ("apple", "banana", "cherry")
print(thistuple1[1])


'''

Negative Indexing

Negative indexing means beginning from the end, -1 refers to the last item, -2 refers to the second last item etc.

'''
# Print the last item of the tuple:
thistuple2 = ("apple", "banana", "cherry")
print(thistuple2[-1])


'''

Range of Indexes

You can specify a range of indexes by specifying where to start and where to end the range.

When specifying a range, the return value will be a new tuple with the specified items.

'''
# Return the third, fourth, and fifth item:
thistuple3 = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple3[2:5])  # Note: The search will start at index 2 (included) and end at index 5 (not included).

# By leaving out the start value, the range will start at the first item:
print(thistuple3[:4])

# By leaving out the end value, the range will go on to the end of the list:
print(thistuple3[2:])


'''

Range of Negative Indexes

Specify negative indexes if you want to start the search from the end of the tuple.

'''
# This example returns the items from index -4 (included) to index -1 (excluded)
thistuple4 = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple4[-4:-1])


'''

Check if Item Exists

To determine if a specified item is present in a tuple use the in keyword:

'''
# Check if "apple" is present in the tuple:
checktuple = ("apple", "banana", "cherry")
if "apple" in checktuple:
    print("Yes, 'apple' is in the fruits tuple")
