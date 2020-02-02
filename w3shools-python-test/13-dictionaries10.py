# Demo Python Dictionaries - Dictionary
'''
Removing Items

There are several methods to remove items from a dictionary.

'''

# The popitem() method removes the last inserted item (in versions before 3.7, a random item is removed instead):
thisdict =	{
    "brand": "TOYOTA",
    "model": "LAND CRUISER",
    "year": 2020,
    "color": "red"
}

print(thisdict)

thisdict.popitem()
print(thisdict) 