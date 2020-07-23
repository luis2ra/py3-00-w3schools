# Demo Python Lists
'''
List

A list is a collection which is ordered and changeable. In Python lists are written with square brackets.


Remove Item

There are several methods to remove items from a list:

- The remove() method removes the specified item.
- The pop() method removes the specified index, (or the last item if index is not specified).
- The del keyword removes the specified index or can also delete the list completely.
- The clear() method empties the list.

'''

# The remove() method removes the specified item:
thislist = ["apple", "banana", "cherry"]
print(thislist)
thislist.remove("banana")
print(thislist)


# The pop() method removes the specified index, (or the last item if index is not specified):
otherlist = ["dog", "cat", "bird", "monkey"]
print(otherlist)
otherlist.pop()
print(otherlist)


# The del keyword removes the specified index:
thislist2 = ["yellow", "blue", "red", "green", "gray"]
print(thislist2)
del thislist2[0]
print(thislist2)


# The del keyword can also delete the list completely:
lista_numeros = ["one", "two", "three", "four", "five"]
print(lista_numeros)
del lista_numeros
print("La variable 'lista_numeros' deja de ser una referencia válida")


# The clear() method empties the list:
lista = ["manzanas", "peras", "fresas", "uvas"]
print(lista)
lista.clear()
print(lista)