# @author: https://github.com/luis2ra from https://www.w3schools.com/python/python_json.asp

# Demo Python JSON - Convert from Python to JSON
'''
Python JSON - Convert from Python to JSON


If you have a Python object, you can convert it into a JSON string by using the json.dumps() method.
'''
import json


# a Python object (dict):
x = {
  "name": "John",
  "age": 30,
  "city": "New York"
}

# convert from Python to JSON:
y = json.dumps(x)

# the result is a JSON string:
print(y)
