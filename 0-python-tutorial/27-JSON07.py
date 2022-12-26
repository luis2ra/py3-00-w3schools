# @author: https://github.com/luis2ra from https://www.w3schools.com/python/python_json.asp

# Demo Python JSON - Order the Result
'''
Python JSON - Order the Result


The json.dumps() method has parameters to order the keys in the result:

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

# Use the sort_keys parameter to specify if the result should be sorted or not:
print(json.dumps(x, indent=4, sort_keys=True))
