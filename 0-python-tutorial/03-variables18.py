# Demo python variables - The global Keyword
'''
The global Keyword

Normally, when you create a variable inside a function, that variable is local, and can only be used inside that function.

To create a global variable inside a function, you can use the global keyword.

Note: Also, use the global keyword if you want to change a global variable inside a function.
'''

# If you use the global keyword, the variable belongs to the global scope:
def myfunc():
    global x
    x = "fantastic"
    print(x)

myfunc()

print("Python is " + x) 