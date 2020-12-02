import re

string1 = "1 2 13 'hello world' 25 'hello world' 14"

c_comilla = "'"
resultado = re.search(c_comilla, string1 )
if resultado is not None:
    print('hay comillas')
    lista_inicial = re.split(' ', string1)
    lista = []
    inicial = 0
    texto = ''
    for elemento in lista_inicial:
        if elemento.find(c_comilla) == -1 and inicial == 0:
            lista.append(elemento)
        elif elemento.find(c_comilla) == 0 and inicial == 0:
            texto = elemento
            inicial = 1
        elif elemento.find(c_comilla) == -1 and inicial == 1:
            texto = texto + ' ' + elemento
        elif elemento.find(c_comilla) == len(elemento) - 1 and inicial == 1:
            texto = texto + ' ' + elemento
            ancho = len(texto)-1
            lista.append(texto[1:int(ancho)])
            inicial = 0
            texto = ''
    print( lista )
else:
    print('no hay comillas')
    lista = re.split(' ', string1)
    print( lista )
