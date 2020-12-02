'''
Digital root is the recursive sum of all the digits in a number.

Given n, take the sum of the digits of n. If that value has more than one digit, 
continue reducing in this way until a single-digit number is produced.
The input will be a non-negative integer.
'''

def digital_root(n):
    lista = str(n)
    suma = 0
    for i in lista:
        suma += int(i)
    if suma < 10:
        return suma
    else:
        return digital_root(suma)

n = input('Ingrese un numero positivo: ')
print('El resultado es: ', digital_root(n))

