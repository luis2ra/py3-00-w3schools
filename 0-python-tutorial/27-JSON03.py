# @author: https://github.com/luis2ra from https://www.w3schools.com/python/python_json.asp

# Demo Python JSON - Convert from Python to JSON
'''
Python JSON - Convert from Python to JSON


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
