# Demo Python Modules - Create and Use a Module
'''
What is a Module?

Consider a module to be the same as a code library.
A file containing a set of functions you want to include in your application.


Create a Module

To create a module just save the code you want in a file with the file extension .py.

Nota: Se genera el archivo files/mymodule.py para efectos de uso en este tutorial.


Use a Module

Now we can use the module we just created, by using the import statement.


Re-naming a Module

You can create an alias when you import a module, by using the 'as' keyword.

'''

import files.mymodule as mymodule

mymodule.greeting("Jonathan")