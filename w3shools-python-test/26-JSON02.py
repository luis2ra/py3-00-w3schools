# Demo Python JSON - Convert from Python to JSON
'''
JSON is a syntax for storing and exchanging data.

JSON is text, written with JavaScript object notation.


JSON in Python
Python has a built-in package called json, which can be used to work with JSON data.


Convert from Python to JSON
If you have a Python object, you can convert it into a JSON string by using the json.dumps() method.


'''

import json

# a Python object (dict):
x = {
  "name": "John",
  "age": 30,
  "city": "New York"
}

# convert into JSON:
y = json.dumps(x)

# the result is a JSON string:
print(y)