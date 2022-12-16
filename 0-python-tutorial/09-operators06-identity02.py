# @author: https://github.com/luis2ra from https://www.w3schools.com/python/python_operators.asp

# Demo Python Operators
'''
Python Operators - Python Identity Operators

Identity operators are used to compare the objects, not if they are equal, but if they are actually the same object, with the same memory location:

Operator 	Description 	                                            Example
is  	    Returns True if both variables are the same object 	        x is y 	
is not 	    Returns True if both variables are not the same object 	    x is not y

'''

x = ["apple", "banana"]
y = ["apple", "banana"]
z = x

print(x is not z)       # returns False because z is the same object as x

print(x is not y)       # returns True because x is not the same object as y, even if they have the same content

print(x != y)           # to demonstrate the difference betweeen "is not" and "!=": this comparison returns False because x is equal to y
