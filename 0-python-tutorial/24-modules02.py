# @author: https://github.com/luis2ra from https://www.w3schools.com/python/python_modules.asp

# Demo Python Modules - Variables in Module
'''
Python Modules - Variables in Module

The module can contain functions, as already described, but also variables of all types (arrays, dictionaries, objects etc).

Nota: Se genera el archivo files/mymodule2.py para efectos de uso en este tutorial.


Naming a Module

You can name the module file whatever you like, but it must have the file extension .py

Re-naming a Module

You can create an alias when you import a module, by using the "as" keyword:

'''
# Import the module named mymodule2, and access the person1 dictionary:
import files.mymodule2 as mymodule  # You can create an alias when you import a module, by using the "as" keyword

a = mymodule.person1["age"]
print(a)
