# Demo Python Modules - Import From Module
'''
Import From Module

You can choose to import only parts from a module, by using the from keyword.

Nota: Se genera el archivo files/mymodule2.py para efectos de uso en este tutorial.

'''

# The module named mymodule has one function and one dictionary:

from files.mymodule2 import person1

print (person1["age"])

# Note: When importing using the from keyword, do not use the module name when referring to elements in the module. 
# Example: person1["age"], not mymodule.person1["age"]
