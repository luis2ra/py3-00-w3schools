# Demo Python Modules - Variables in Module
'''
Variables in Module

The module can contain functions, as already described, but also variables of all types (arrays, dictionaries, objects etc).

Nota: Se genera el archivo files/mymodule2.py para efectos de uso en este tutorial.


'''

# Import the module named mymodule2, and access the person1 dictionary:

import files.mymodule2 as mymodule

a = mymodule.person1["age"]
print(a) 