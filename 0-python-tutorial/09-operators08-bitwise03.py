# @author: https://github.com/luis2ra from https://www.w3schools.com/python/python_operators.asp

# Demo Python Operators
'''
Python Operators - Python Bitwise Operators

~  	        NOT 	                Inverts all the bits

'''

a = 60
b = 13

variable1 = ~a
variable2 = ~b

print("Variable 'a': ", a, "Variable 'a' en binario: ", format(a, 'b'))
print("Procesando '~a': ", variable1, "Resultado en binario: ", format(variable1, 'b'))
print("Variable 'b': ", b, "Variable 'b' en binario: ", format(b, 'b'))
print("Procesando '~b': ", variable2, "Resultado en binario: ", format(variable2, 'b'))

print("Procesando 'a & b': ", a&b, "Resultado en binario: ", format(a&b, 'b'))
print("Procesando 'a | b': ", a|b, "Resultado en binario: ", format(a|b, 'b'))
print("Procesando 'a ^ b': ", a^b, "Resultado en binario: ", format(a^b, 'b'))
