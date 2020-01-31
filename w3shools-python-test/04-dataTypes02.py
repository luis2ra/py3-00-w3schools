# Demo Python Data Types - Setting the Data Type
'''
Built-in Data Types

In programming, data type is an important concept.

Variables can store data of different types, and different types can do different things.

Python has the following data types built-in by default, in these categories:
Text Type: 	        str
Numeric Types: 	    int, float, complex
Sequence Types: 	list, tuple, range
Mapping Type: 	    dict
Set Types: 	        set, frozenset
Boolean Type: 	    bool
Binary Types: 	    bytes, bytearray, memoryview
'''

# In Python, the data type is set when you assign a value to a variable:
# Data Type : str
x1 = "Hello World"
print(x1)
print(type(x1))

# Data Type : int
x2 = 20
print(x2)
print(type(x2))

# Data Type : float
x3 = 20.5
print(x3)
print(type(x3))

# Data Type : complex
x4 = 1j
print(x4)
print(type(x4))

# Data Type : list
x5 = ["apple", "banana", "cherry"]
print(x5)
print(type(x5))

# Data Type : tuple
x6 = ("apple", "banana", "cherry")
print(x6)
print(type(x6))

# Data Type : range
x7 = range(6)
print(x7)
print(type(x7))

# Data Type : dict
x8 = {"name" : "John", "age" : 36}
print(x8)
print(type(x8))

# Data Type : set
x9 = {"apple", "banana", "cherry"}
print(x9)
print(type(x9))

# Data Type : frozenset
x10 = frozenset({"apple", "banana", "cherry"})
print(x10)
print(type(x10))

# Data Type : bool
x11 = True
print(x11)
print(type(x11))

# Data Type : bytes
x12 = b"Hello"
print(x12)
print(type(x12))

# Data Type : bytearray
x13 = bytearray(5)
print(x13)
print(type(x13))

# Data Type : memoryview
x14 = memoryview(bytes(5))
print(x14)
print(type(x14))
