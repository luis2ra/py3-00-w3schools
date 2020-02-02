# Demo Python JSON - Convert from Python to JSON
'''
JSON is a syntax for storing and exchanging data.

JSON is text, written with JavaScript object notation.


JSON in Python
Python has a built-in package called json, which can be used to work with JSON data.


Convert from Python to JSON
If you have a Python object, you can convert it into a JSON string by using the json.dumps() method.

You can convert Python objects of the following types, into JSON strings:

* dict
* list
* tuple
* string
* int
* float
* True
* False
* None

'''

import json

# Python dict -> JSON Object 
print(json.dumps({"name": "John", "age": 30}))

# Python list -> JSON Array
print(json.dumps(["apple", "bananas"]))

# Python tuple -> JSON Array
print(json.dumps(("apple", "bananas")))

# Python str -> JSON String
print(json.dumps("hello"))

# Python ing -> JSON Number
print(json.dumps(42))

# Python float -> JSON Number
print(json.dumps(31.76))

# Python True -> JSON true
print(json.dumps(True))

# Python False -> JSON false
print(json.dumps(False))

# Python None -> JSON null
print(json.dumps(None))
