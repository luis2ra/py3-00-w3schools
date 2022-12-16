# @author: https://github.com/luis2ra from https://www.w3schools.com/python/python_booleans.asp

# Demo Python Booleans - Some Values are False
'''
Some Values are False

In fact, there are not many values that evaluates to False, except empty values, 
such as (), [], {}, "", the number 0, and the value None. And of course the value False evaluates to False.

'''

# The following will return False:
print( bool(False) )
print( bool(None) )
print( bool("") )
print( bool(0) )
print( bool([]) )   # list
print( bool(()) )   # tuple
print( bool({}) )   # set / dictionary

# print( type( [] ) )     # reconoce una lista vacía
# print( type( () ) )     # reconoce una tupla vacía
# print( type( {} ) )     # reconoce un diccionario vacío
