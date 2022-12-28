# @author: https://github.com/luis2ra from https://www.w3schools.com/python/python_dictionaries_change.asp

# Demo Change Dictionary Items
'''
Python Dictionaries - Change Dictionary Items


Change Values

You can change the value of a specific item by referring to its key name:

'''
# Change the "year" to 2018:
thisdict =	{
    "brand": "TOYOTA",
    "model": "LAND CRUISER",
    "year": 2020
}
thisdict["year"]=2018
print(thisdict)


'''

Update Dictionary

The update() method will update the dictionary with the items from the given argument.

The argument must be a dictionary, or an iterable object with key:value pairs.

'''
# Update the "year" of the car by using the update() method:
thisdict2 = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
thisdict2.update({"year": 2020})

print(thisdict2)
