# Demo Python JSON - Convert from Python to JSON
'''
Convert from Python to JSON
If you have a Python object, you can convert it into a JSON string by using the json.dumps() method.


Order the Result
The json.dumps() method has parameters to order the keys in the result:

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

# sort the result alphabetically by keys:
print(json.dumps(x, indent=4, sort_keys=True))