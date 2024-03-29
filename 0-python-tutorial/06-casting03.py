# @author: https://github.com/luis2ra from https://www.w3schools.com/python/python_casting.asp

# Demo Python Casting - Specify a Variable Type
'''
Python Casting


Specify a Variable Type

There may be times when you want to specify a type on to a variable. This can be done with casting.
Python is an object-orientated language, and as such it uses classes to define data types, including its primitive types.

Casting in python is therefore done using constructor functions:

int() - constructs an integer number from an integer literal, a float literal (by rounding down to the previous whole number), or a string literal (providing the string represents a whole number).

float() - constructs a float number from an integer literal, a float literal or a string literal (providing the string represents a float or an integer).

str() - constructs a string from a wide variety of data types, including strings, integer literals and float literals.

'''
# Strings:
x = str("s1") # x will be 's1'
y = str(2)    # y will be '2'
z = str(3.0)  # z will be '3.0' 

print(x)
print(y)
print(z)
print(x + y + z + x)
print(x, y, z, x)
