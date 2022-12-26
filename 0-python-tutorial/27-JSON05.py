# @author: https://github.com/luis2ra from https://www.w3schools.com/python/python_json.asp

# Demo Python JSON - Format the Result
'''
Python JSON - Format the Result


The example preview prints a JSON string, but it is not very easy to read, with no indentations and line breaks.

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
