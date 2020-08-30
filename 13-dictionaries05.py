# Demo Python Dictionaries - Dictionary
'''
Loop Through a Dictionary

You can loop through a dictionary by using a for loop.

When looping through a dictionary, the return value are the keys of the dictionary, but there are methods to return the values as well.

'''

# Print all key names in the dictionary, one by one:
thisdict =	{
    "brand": "TOYOTA",
    "model": "LAND CRUISER",
    "year": 2020
}

print(thisdict)
for x in thisdict:
    print(x)


# Print all values in the dictionary, one by one:
for x in thisdict:
    print(thisdict[x])


# You can also use the values() function to return values of a dictionary:
for x in thisdict.values():
    print(x)


# Loop through both keys and values, by using the items() function:
for x, y in thisdict.items():
    print(x, y) 