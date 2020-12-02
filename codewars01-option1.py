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
    return suma


n = input('Ingrese un numero positivo: ')
flag = 0
while True:
    if flag == 0:
        result = digital_root(n)
        flag = 1
    else:
        if result < 10:
            break
        else:
            result = digital_root(result)

print('El resultado es: ', result)