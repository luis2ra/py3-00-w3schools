# Demo Python Modules - Using the dir() Function
'''
Using the dir() Function

There is a built-in function to list all the function names (or variable names) in a module. The dir() function.

Note: The dir() function can be used on all modules, also the ones you create yourself.

'''

# List all the defined names belonging to the platform module

import platform

x = dir(platform)
print(x)