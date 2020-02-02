# Demo Python Dictionaries - Dictionary
'''
Change Values

You can change the value of a specific item by referring to its key name.

'''

# There is also a method called get() that will give you the same result:
thisdict =	{
    "brand": "TOYOTA",
    "model": "LAND CRUISER",
    "year": 2020
}
x = thisdict.get("model")
print(x)