# @author: https://github.com/luis2ra from https://www.w3schools.com/python/python_scope.asp

# Demo Python Scope
'''
Python Scope - Python Scope


A variable is only available from inside the region it is created. This is called scope.

Local Scope

A variable created inside a function belongs to the local scope of that function, and can only be used inside that function.


Global Scope

A variable created in the main body of the Python code is a global variable and belongs to the global scope.
Global variables are available from within any scope, global and local.


Global Keyword

If you need to create a global variable, but are stuck in the local scope, you can use the global keyword.
The global keyword makes the variable global.

'''
# A variable created inside a function is available inside that function:
def myfunc():
    x = 300
    print(x)

myfunc()
