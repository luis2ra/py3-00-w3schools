# @author: https://github.com/luis2ra from https://www.w3schools.com/python/python_scope.asp

# Demo Python Scope - Global Scope
'''
Python Scope - Global Scope

A variable created in the main body of the Python code is a global variable and belongs to the global scope.

Global variables are available from within any scope, global and local.

'''
# A variable created outside of a function is global and can be used by anyone:
x = 300

def myfunc():
    print(x)

myfunc()
print(x)
