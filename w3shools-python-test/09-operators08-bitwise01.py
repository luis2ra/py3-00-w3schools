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

compara1 = 1 | 1
compara2 = 1 | 0
compara3 = 0 | 1
compara4 = 0 | 0
print("Uso de operador & ", compara1)
print("Uso de operador & ", compara2)
print("Uso de operador & ", compara3)
print("Uso de operador & ", compara4)

compara1 = 1 | 1
compara2 = 1 | 0
compara3 = 0 | 1
compara4 = 0 | 0
print("Uso de operador | ", compara1)
print("Uso de operador | ", compara2)
print("Uso de operador | ", compara3)
print("Uso de operador | ", compara4)

compara1 = 1 ^ 1
compara2 = 1 ^ 0
compara3 = 0 ^ 1
compara4 = 0 ^ 0
print("Uso de operador ^ ", compara1)
print("Uso de operador ^ ", compara2)
print("Uso de operador ^ ", compara3)
print("Uso de operador ^ ", compara4)

variable1 = 0
variable2 = 1
print("Uso de operador ~ ", ~variable1)
print("validando formato resultado: ", format(~variable1, 'b'))
print("Uso de operador ~ ", ~variable2)
print("validando el formato del resultado: ", format(~variable2, 'b'))

compara1 = 1 >> 1
compara2 = 1 >> 0
compara3 = 0 >> 1
compara4 = 0 >> 0
print("Uso de operador >> ", compara1)
print("Uso de operador >> ", compara2)
print("Uso de operador >> ", compara3)
print("Uso de operador >> ", compara4)

compara1 = 1 << 1
compara2 = 1 << 0
compara3 = 0 << 1
compara4 = 0 << 0
print("Uso de operador << ", compara1)
print("Uso de operador << ", compara2)
print("Uso de operador << ", compara3)
print("Uso de operador << ", compara4)