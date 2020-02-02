# Demo Python JSON - Convert from Python to JSON
'''
Convert from Python to JSON
If you have a Python object, you can convert it into a JSON string by using the json.dumps() method.

'''

import json

# Convert a Python object containing all the legal data types: 

x = {
    "name": "John",
    "age": 30,
    "married": True,
    "divorced": False,
    "children": ("Ann","Billy"),
    "pets": None,
    "cars": [
        {"model": "BMW 230", "mpg": 27.5},
        {"model": "Ford Edge", "mpg": 24.1}
    ]
}

# convert into JSON:
y = json.dumps(x)

# the result is a JSON string:
print(y)