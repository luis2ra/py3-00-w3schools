# @author: https://github.com/luis2ra from https://www.w3schools.com/python/python_modules.asp

# Demo Python Modules - Using the dir() Function
'''
Python Modules - Using the dir() Function

There is a built-in function to list all the function names (or variable names) in a module. The dir() function.

Note: The dir() function can be used on all modules, also the ones you create yourself.

'''
# List all the defined names belonging to the platform module
import platform
import files.mymodule2

x = dir(platform)
print(x)

print()
print(dir(files.mymodule2))
