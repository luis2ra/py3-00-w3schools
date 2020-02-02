# Demo Python Dictionaries - Dictionary
'''
Copy a Dictionary

You cannot copy a dictionary simply by typing dict2 = dict1, because: dict2 will only be a reference to dict1, and changes made in dict1 will automatically also be made in dict2.

There are ways to make a copy, one way is to use the built-in Dictionary method copy().

Another way to make a copy is to use the built-in method dict().

'''

# Make a copy of a dictionary with the dict() method:
mydict =	{
    "brand": "TOYOTA",
    "model": "LAND CRUISER",
    "year": 2020,
    "color": "red"
}

print(mydict)

mycopy = dict(mydict)
print(mycopy)