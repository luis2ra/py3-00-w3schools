# Demo Python Dictionaries - Dictionary
'''
Removing Items

There are several methods to remove items from a dictionary.

'''

# The del keyword removes the item with the specified key name:
thisdict =	{
    "brand": "TOYOTA",
    "model": "LAND CRUISER",
    "year": 2020,
    "color": "red"
}

print(thisdict)

del thisdict["model"]
print(thisdict) 