'''
Python MongoDB Find

* In MongoDB we use the find and findOne methods to find data in a collection.
* Just like the SELECT statement is used to find data in a table in a MySQL database.


Find All

To select data from a table in MongoDB, we can also use the find() method.

The find() method returns all occurrences in the selection.

The first parameter of the find() method is a query object. In this example we use an empty query object, which selects all documents in the collection.

'''
import pymongo

myclient = pymongo.MongoClient('mongodb://localhost:27017/')
mydb = myclient['w3schools-myDatabase']
mycollection = mydb["customers"]

# Return all documents in the "customers" collection, and print each document:
for x in mycollection.find():
    print(x)

print('\n')
# Otra alternativa
lista = mycollection.find()
for y in lista:
    print(y)