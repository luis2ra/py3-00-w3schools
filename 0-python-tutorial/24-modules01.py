# @author: https://github.com/luis2ra from https://www.w3schools.com/python/python_modules.asp

# Demo Python Modules - Create and Use a Module
'''
Python Modules


What is a Module?

Consider a module to be the same as a code library.

A file containing a set of functions you want to include in your application.


Create a Module

To create a module just save the code you want in a file with the file extension .py.

Nota: Se genera el archivo files/mymodule.py para efectos de uso en este tutorial.


Use a Module

Now we can use the module we just created, by using the import statement.


Re-naming a Module

You can create an alias when you import a module, by using the "as" keyword.

'''
# Import the module named mymodule
import files.mymodule as mymodule

# call the greeting function that is defined within the module
mymodule.greeting("Jonathan")  # Note: When using a function from a module, use the syntax: module_name.function_name.
