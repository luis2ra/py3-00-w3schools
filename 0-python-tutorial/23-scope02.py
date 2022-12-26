# @author: https://github.com/luis2ra from https://www.w3schools.com/python/python_scope.asp

# Demo Python Scope - Function Inside Function
'''
Python Scope - Function Inside Function

As explained in the example preview, the variable x is not available outside the function, but it is available for any function inside the function:

'''
# The local variable can be accessed from a function within the function:
def myfunc():
    x = 300

    def myinnerfunc():
        print(x)
    
    myinnerfunc()

myfunc()
