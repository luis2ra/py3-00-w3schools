# @author: https://github.com/luis2ra from https://www.w3schools.com/python/python_json.asp

# Demo Python JSON - JSON in Python
'''
Python JSON


JSON is a syntax for storing and exchanging data.

JSON is text, written with JavaScript object notation.


JSON in Python

Python has a built-in package called "json", which can be used to work with JSON data.

Example - Import the json module:
import json


Parse JSON - Convert from JSON to Python

If you have a JSON string, you can parse it by using the json.loads() method. The result will be a Python dictionary.
'''
import json


# some JSON string:
x = '{ "name":"John", "age":30, "city":"New York"}'

# parse x:
y = json.loads(x)

# the result is a Python dictionary:
print(y["age"])
