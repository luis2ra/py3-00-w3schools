# @author: https://github.com/luis2ra from https://www.w3schools.com/python/python_dictionaries_copy.asp

# Demo Copy Dictionaries
'''
Python Dictionaries - Copy Dictionaries


Copy a Dictionary

You cannot copy a dictionary simply by typing dict2 = dict1, because: dict2 will only be 
a reference to dict1, and changes made in dict1 will automatically also be made in dict2.

There are ways to make a copy, one way is to use the built-in Dictionary method copy().

'''
# Make a copy of a dictionary with the copy() method:
mydict =	{
    "brand": "TOYOTA",
    "model": "LAND CRUISER",
    "year": 2020,
    "color": "red"
}
print(mydict)

my_copy1 = mydict.copy()

mydict["year"] = 2022
print('checking the copy: ', my_copy1)
print('checking the original: ', mydict)

print()

# Another way to make a copy is to use the built-in function dict().
thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
print(thisdict)

my_copy2 = dict(thisdict)
print(my_copy2)
