# @author: https://github.com/luis2ra from 

# Demo Access Dictionary Items
'''
Python Dictionaries - Access Dictionary Items


Accessing Items

You can access the items of a dictionary by referring to its key name, inside square brackets:
'''
# Get the value of the "model" key:
thisdict1 =	{
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
x = thisdict1["model"]
print(x)


# There is also a method called get() that will give you the same result:
thisdict2 =	{
    "brand": "TOYOTA",
    "model": "LAND CRUISER",
    "year": 2020
}
x = thisdict2.get("model")
print(x)


'''
Get Keys

The keys() method will return a list of all the keys in the dictionary.
'''
# Get a list of the keys:
thisdict3 = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
x = thisdict3.keys()
print(x)

# The list of the keys is a view of the dictionary, meaning that any changes done to the dictionary will be reflected in the keys list.
car = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
y = car.keys()
print(y)  # before the change

car["color"] = "white"
print(y)  # after the change


'''
Get Values

The values() method will return a list of all the values in the dictionary.
'''
# Get a list of the values:
thisdict4 = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
z = thisdict4.values()
print(z)

# The list of the values is a view of the dictionary, meaning that any changes done to the dictionary will be reflected in the values list.
car2 = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
y2 = car2.values()
print(y2)  # before the change

car2["year"] = 2020
print(y2)  # after the change


# Add a new item to the original dictionary, and see that the values list gets updated as well:
car3 = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}

y3 = car3.values()
print(y3)  # before the change

car3["color"] = "red"
print(y3)  # after the change


'''
Get Items

The items() method will return each item in a dictionary, as tuples in a list.
'''
# Get a list of the key:value pairs
thisdict5 = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

p = thisdict5.items()
print(p)


# The returned list is a view of the items of the dictionary, meaning that any changes done to the dictionary will be reflected in the items list.
car4 = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}

x4 = car4.items()
print(x4)  # before the change

car4["year"] = 2020
print(x4)  # after the change


# Add a new item to the original dictionary, and see that the items list gets updated as well:
car5 = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}

x5 = car5.items()
print(x5)  # before the change

car5["color"] = "red"
print(x5)  # after the change


'''
Check if Key Exists

To determine if a specified key is present in a dictionary use the 'in' keyword.

'''
# Check if "model" is present in the dictionary:
thisdict =	{
    "brand": "TOYOTA",
    "model": "LAND CRUISER",
    "year": 2020
}

if "model" in thisdict:
    print("Yes, 'model' is one of the keys in the thisdict dictionary")
