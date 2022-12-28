# @author: https://github.com/luis2ra from https://www.w3schools.com/python/python_dictionaries_remove.asp

# Demo Remove Dictionary Items
'''
Python Dictionaries - Remove Dictionary Items


Removing Items

There are several methods to remove items from a dictionary:

'''
# The pop() method removes the item with the specified key name:
thisdict =	{
    "brand": "TOYOTA",
    "model": "LAND CRUISER",
    "year": 2020,
    "color": "red"
}
print(thisdict)  # before removing

thisdict.pop("model")
print(thisdict)  # after removing


# The popitem() method removes the last inserted item (in versions before 3.7, a random item is removed instead):
thisdict2 =	{
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
print(thisdict2)  # before removing

thisdict2.popitem()
print(thisdict2)  # after removing


# The clear() keyword empties the dictionary:
thisdict3 =	{
    "brand": "TOYOTA",
    "model": "LAND CRUISER",
    "year": 2020,
    "color": "red"
}

print(thisdict3)  # before removing

thisdict3.clear()
print(thisdict3)  # after removing


# The del keyword removes the item with the specified key name:
thisdict4 =	{
    "brand": "TOYOTA",
    "model": "LAND CRUISER",
    "year": 2020,
    "color": "red"
}

print(thisdict4)  # before removing

del thisdict4["model"]
print(thisdict4)  # after removing


# The del keyword can also delete the dictionary completely:
thisdict5 =	{
    "brand": "TOYOTA",
    "model": "LAND CRUISER",
    "year": 2020,
    "color": "red"
}

print(thisdict5)

del thisdict5
print(thisdict5)  # This cause an Error => NameError: name 'thisdict5' is not defined.
