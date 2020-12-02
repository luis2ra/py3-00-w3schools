'''
Python MongoDB Insert Document

A document in MongoDB is the same as a record in SQL databases.


Insert Into Collection

To insert a record, or document as it is called in MongoDB, into a collection, we use the insert_one() method.

The first parameter of the insert_one() method is a dictionary containing the name(s) and value(s) of each field in the document you want to insert.

'''
import pymongo

myclient = pymongo.MongoClient('mongodb://localhost:27017/')
mydb = myclient['w3schools-myDatabase']
mycollection = mydb["customers"]

mydict = { "name": "John", "address": "Highway 37" }

# Insert a record in the "customers" collection:
x = mycollection.insert_one(mydict)

print(x)

