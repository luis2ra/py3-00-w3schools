# Demo Remove List Items
'''
Remove Item

There are several methods to remove items from a list:

- The remove() method removes the specified item.
- The pop() method removes the specified index, (or the last item if index is not specified).
- The del keyword removes the specified index or can also delete the list completely.
- The clear() method empties the list.

'''

# The remove() method removes the specified item:
thislist = ["apple", "banana", "cherry"]
print('before: ', thislist)
thislist.remove("banana")
print('after: ', thislist)


# The pop() method removes the specified index, (or the last item if index is not specified):
pets_list = ["dog", "cat", "bird", "monkey"]
print('before: ', pets_list)
pets_list.pop(1)
print('after', pets_list)

otherlist = ["dog", "cat", "bird", "monkey"]
print('before: ', otherlist)
otherlist.pop()
print('after', otherlist)


# The del keyword removes the specified index:
thislist2 = ["yellow", "blue", "red", "green", "gray"]
print('before: ', thislist2)
del thislist2[0]
print(thislist2)


# The del keyword can also delete the list completely:
lista_numeros = ["one", "two", "three", "four", "five"]
print('before: ', lista_numeros)
del lista_numeros
print("La variable 'lista_numeros' deja de ser una referencia válida")


# The clear() method empties the list:
lista = ["manzanas", "peras", "fresas", "uvas"]
print('before: ', lista)
lista.clear()
print(lista)