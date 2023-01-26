lista = [8, 9, 3]
print(lista)
print(len(lista))
simbolo = ""

for i in range(len(lista)):
    aux = lista[i]
    izq = 0
    der = i - 1
    print('i', i)
    print('aux', aux)
    print('izq', izq)
    print('der', der)

    j = i - 1
    print('j', j)

simbolo[i-1] = "$"
print('i', i)
salida = ""
print('simbolo', simbolo)
print('salida', salida)