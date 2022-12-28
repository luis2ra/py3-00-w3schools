# @author: https://github.com/luis2ra from https://www.w3schools.com/python/python_booleans.asp

# Demo Python Booleans - Most Values are True
'''
Most Values are True

Almost any value is evaluated to True if it has some sort of content.

Any string is True, except empty strings.

Any number is True, except 0.

Any list, tuple, set, and dictionary are True, except empty ones.

'''
# The following will return True:
print( bool("abc") )
print( bool(123) )
print( bool(["apple", "cherry", "banana"]) )    # list
print( bool(("apple", "banana", "cherry")) )    # tuple
print( bool({"apple", "banana", "cherry"}) )    # set
print( bool({"brand": "Ford", "model": "Mustang", "year": 1964}) )  # dictionary
