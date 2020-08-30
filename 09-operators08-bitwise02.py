# Demo Python Operators
'''
Python Bitwise Operators

Bitwise operators are used to compare (binary) numbers:

Operator 	Name 	                Description
&  	        AND 	                Sets each bit to 1 if both bits are 1
| 	        OR 	                    Sets each bit to 1 if one of two bits is 1
^ 	        XOR 	                Sets each bit to 1 if only one of two bits is 1
~  	        NOT 	                Inverts all the bits
<< 	        Zero fill left shift 	Shift left by pushing zeros in from the right and 
                                    let the leftmost bits fall off
>> 	        Signed right shift 	    Shift right by pushing copies of the leftmost bit in 
                                    from the left, and let the rightmost bits fall off

'''

a = 5
b = 3
c = 2
d = 4

compara1 = a & b
compara2 = a & c
compara3 = c & d

print("Variable a: ", a, "En binario: ", format(a, 'b'))
print("Variable b: ", b, "En binario: ", format(b, 'b'))
print("Procesando a & b", compara1, "Resultado en binario: ", format(compara1, 'b'))
print("Uso de operador &", compara2)
print("Uso de operador &", compara3)

compara1 = a | b
compara2 = a | c
compara3 = c | d
print("Uso de operador | ", compara1)
print("Uso de operador | ", compara2)
print("Uso de operador | ", compara3)

compara1 = a ^ b
compara2 = a ^ c
compara3 = c ^ d
print("Uso de operador ^ ", compara1)
print("Uso de operador ^ ", compara2)
print("Uso de operador ^ ", compara3)

variable1 = ~a
variable2 = ~b
variable3 = ~c
print("Variable 'a': ", a, "Variable 'a' en binario: ", format(a, 'b'))
print("Procesando '~a': ", variable1, "Resultado en binario: ", format(variable1, 'b'))
print("Variable 'b': ", b, "Variable 'b' en binario: ", format(b, 'b'))
print("Procesando '~b': ", variable2, "Resultado en binario: ", format(variable2, 'b'))
print("Variable 'c': ", c, "Variable 'c' en binario: ", format(c, 'b'))
print("Procesando '~c': ", variable3, "Resultado en binario: ", format(variable3, 'b'))

compara1 = a >> b
compara2 = a >> c
compara3 = c >> d
print("Uso de operador >> ", compara1)
print("Uso de operador >> ", compara2)
print("Uso de operador >> ", compara3)

compara1 = a << b
compara2 = a << c
compara3 = c << d
print("Uso de operador << ", compara1)
print("Uso de operador << ", compara2)
print("Uso de operador << ", compara3)