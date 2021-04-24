# @author: https://github.com/luis2ra from https://www.w3schools.com/python/python_lists.asp
'''
Python Collections (Arrays)

There are four collection data types in the Python programming language:

*	List is a collection which is ordered and changeable. Allows duplicate members.
*	Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
*	Set is a collection which is unordered and unindexed. No duplicate members.
*	Dictionary is a collection which is ordered (note **) and changeable. No duplicate members.

** As of Python version 3.7, dictionaries are ordered. In Python 3.6 and earlier, dictionaries are unordered.

When choosing a collection type, it is useful to understand the properties of that type. 
Choosing the right type for a particular data set could mean retention of meaning, and, 
it could mean an increase in efficiency or security.


List

Lists are used to store multiple items in a single variable.

Lists are one of 4 built-in data types in Python used to store collections of data, the other 3 are 
Tuple, Set, and Dictionary, all with different qualities and usage.

Lists are created using square brackets.


Check if Item Exists

To determine if a specified item is present in a list use the 'in' keyword.

'''

# Create a List:
thislist = ["apple", "banana", "cherry"]
print(thislist)


# Check if "mango" is present in the list:
list2 = ["apple", "banana", "cherry", "mango"]
if "mango" in list2:
    print("Yes, 'mango' is in the fruits list") 

if "lemon" in list2:
    print("Yes, 'lemon' is in the fruits list") 
else:
    print("No, 'lemon' not is in the fruits list") 