# @author: https://github.com/luis2ra from https://www.w3schools.com/python/python_variables_global.asp

# Demo python variables - The global Keyword
'''
The global Keyword

Normally, when you create a variable inside a function, that variable is local, and can only be used inside that function.

To create a global variable inside a function, you can use the global keyword.

Note: Also, use the global keyword if you want to change a global variable inside a function.
'''

# To change the value of a global variable inside a function, refer to the variable by using the global keyword:
x = "awesome"
print('value initial of x: ' + x)

def myfunc():
    global x
    x = "fantastic"
    print('new value of x: ' + x)

myfunc()

print("Python is " + x)
