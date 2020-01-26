# Demo Python Dictionaries
'''
Dictionary
A dictionary is a collection which is unordered, changeable and indexed. In Python dictionaries are written with curly brackets, and they have keys and values.

Loop Through a Dictionary
You can loop through a dictionary by using a for loop.
When looping through a dictionary, the return value are the keys of the dictionary, but there are methods to return the values as well.

Check if Key Exists
To determine if a specified key is present in a dictionary use the in keyword:

Dictionary Length
To determine how many items (key-value pairs) a dictionary has, use the len() method.

Adding Items
Adding an item to the dictionary is done by using a new index key and assigning a value to it.

Removing Items
There are several methods to remove items from a dictionary: pop(), popitem(), del, clear()

Copy a Dictionary
You cannot copy a dictionary simply by typing dict2 = dict1, because: dict2 will only be a reference to dict1, and changes made in dict1 will automatically also be made in dict2.
There are ways to make a copy, one way is to use the built-in Dictionary method copy(). Another way to make a copy is to use the built-in method dict().
 
Nested Dictionaries
A dictionary can also contain many dictionaries, this is called nested dictionaries.

The dict() Constructor
It is also possible to use the dict() constructor to make a new dictionary:

Dictionary Methods
Python has a set of built-in methods that you can use on dictionaries.

clear()	        Removes all the elements from the dictionary
copy()	        Returns a copy of the dictionary
fromkeys()	    Returns a dictionary with the specified keys and values
get()	        Returns the value of the specified key
items()	        Returns a list containing a tuple for each key value pair
keys()	        Returns a list containing the dictionary's keys
pop()	        Removes the element with the specified key
popitem()	    Removes the last inserted key-value pair
setdefault()	Returns the value of the specified key. If the key does not exist: insert the key, with the specified value
update()	    Updates the dictionary with the specified key-value pairs
values()	    Returns a list of all the values in the dictionary

'''