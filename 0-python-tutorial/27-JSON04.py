# @author: https://github.com/luis2ra from https://www.w3schools.com/python/python_json.asp

# Demo Python JSON - Convert from Python to JSON
'''
Python JSON - Convert from Python to JSON


When you convert from Python to JSON, Python objects are converted into the JSON (JavaScript) equivalent:

Python	---------   JSON

dict	            Object
list	            Array
tuple	            Array
str	                String
int	                Number
float	            Number
True	            true
False	            false
None	            null

'''
# Convert a Python object containing all the legal data types: 
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

# convert into JSON:
y = json.dumps(x)

# the result is a JSON string:
print(y)
