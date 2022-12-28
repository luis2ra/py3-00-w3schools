# @author: https://github.com/luis2ra from https://www.w3schools.com/python/python_lists_access.asp

# Demo Access List Items
'''
Python Lists - Access List Items


Access Items

You access the list items by referring to the index number.

Note: The first item has index 0.

'''
# Print the second item of the list:
thislist = ["apple", "banana", "cherry"]
print(thislist[1])


'''
Negative Indexing

Negative indexing means beginning from the end, -1 refers to the last item, -2 refers to the second last item etc.
'''
# Print the last item of the list:
print(thislist[-1])


'''
Range of Indexes

You can specify a range of indexes by specifying where to start and where to end the range.
When specifying a range, the return value will be a new list with the specified items.

'''
# Return the third, fourth, and fifth item:
otherlist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(otherlist[2:5])  # Note: The search will start at index 2 (included) and end at index 5 (not included).
# Remember that the first item is index 0

# By leaving out the start value, the range will start at the first item:
print(otherlist[:4])  # This example returns the items from the beginning to "orange"

# By leaving out the end value, the range will go on to the end of the list:
print(otherlist[2:])  # This example returns the items from "cherry" and to the end


'''
Range of Negative Indexes

Specify negative indexes if you want to start the search from the end of the list.

'''
# This example returns the items from index -4 (included) to index -1 (excluded)
print(otherlist[-4:-1])


'''
Check if Item Exists

To determine if a specified item is present in a list use the 'in' keyword.

'''
# Check if "apple" is present in the list:
list_to_check = ["apple", "banana", "cherry"]
if "apple" in list_to_check:
    print("Yes, 'apple' is in the fruits list")


'''
Challenge: Se necesitaba dividir una lista en bloques de 25, por limitaciones de
la libreria de googlemaps para determinar la mejor ruta.

'''
# Particionar una lista en bloques de 5
list2 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]

partes = len(list2)//5
residuo = len(list2)%5

if residuo > 0:
    for i in range(partes+1):
        print('bloques ', list2[5*i:5*(i+1)])
else:
    for i in range(partes):
        print('bloques ', list2[5*i:5*(i+1)])
