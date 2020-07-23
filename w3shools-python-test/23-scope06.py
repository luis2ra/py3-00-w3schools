# Demo Python Scope - Global Keyword
'''
Global Keyword

If you need to create a global variable, but are stuck in the local scope, you can use the global keyword.

The global keyword makes the variable global.

Also, use the global keyword if you want to make a change to a global variable inside a function.

'''

# To change the value of a global variable inside a function, refer to the variable by using the global keyword:
x = 300

def myfunc():
    global x
    x = 200

myfunc()

print(x)


