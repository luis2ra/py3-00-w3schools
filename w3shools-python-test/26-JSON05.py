# Demo Python JSON - Convert from Python to JSON
'''
Convert from Python to JSON
If you have a Python object, you can convert it into a JSON string by using the json.dumps() method.


Format the Result
The example above prints a JSON string, but it is not very easy to read, with no indentations and line breaks.
The json.dumps() method has parameters to make it easier to read the result.

'''

import json

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

# use four indents to make it easier to read the result:
print(json.dumps(x, indent=4))