# @author: https://github.com/luis2ra from https://www.w3schools.com/python/python_lists_remove.asp

# Demo Remove List Items
'''
Python Lists - Remove List Items


Remove Specified Item

The remove() method removes the specified item.

'''
# Remove "banana":
thislist = ["apple", "banana", "cherry"]
print('before: ', thislist)
thislist.remove("banana")
print('after: ', thislist)


'''
Remove Specified Index

The pop() method removes the specified index.

'''
# Remove the second item:
pets_list = ["dog", "cat", "bird", "monkey"]
print('before: ', pets_list)
pets_list.pop(1)
print('after: ', pets_list)

# If you do not specify the index, the pop() method removes the last item: 
otherlist = ["dog", "cat", "bird", "monkey"]
print('before: ', otherlist)
otherlist.pop()
print('after: ', otherlist)


'''
Remove Specified Index using 'del' keyword

The del keyword also removes the specified index.

The del keyword can also delete the list completely.
'''
# Remove the first item:
thislist2 = ["yellow", "blue", "red", "green", "gray"]
print('before: ', thislist2)
del thislist2[0]
print('after: ', thislist2)


# Delete the entire list:
lista_numeros = ["one", "two", "three", "four", "five"]
print('before: ', lista_numeros)
del lista_numeros
#  NameError: name 'lista_numeros' is not defined


'''
Clear the List

The clear() method empties the list.

The list still remains, but it has no content.
'''
# Clear the list content:
lista = ["manzanas", "peras", "fresas", "uvas"]
print('before: ', lista)
lista.clear()
print('after: ', lista)
