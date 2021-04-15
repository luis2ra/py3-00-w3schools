# Ejercicio que realiza el equivalente al mapeo de un string en javascript

def map_string(cadena):
    mapa = {}
    for key, value in enumerate(cadena):
        if value in mapa:
            mapa[value].append(key)
        else:
            mapa[value] = [key]
    return mapa

string1 = input("Ingrese la cadena a mapear: ")
print("La cadena es: ", string1)
print(map_string(string1))

