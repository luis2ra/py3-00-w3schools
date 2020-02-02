# Demo Python Dictionaries - Dictionary
'''
Removing Items

There are several methods to remove items from a dictionary.

'''

# The 'del' keyword can also delete the dictionary completely:
thisdict =	{
    "brand": "TOYOTA",
    "model": "LAND CRUISER",
    "year": 2020,
    "color": "red"
}

print(thisdict)

del thisdict
print(thisdict)     #this will cause an error because "thisdict" no longer exists. 