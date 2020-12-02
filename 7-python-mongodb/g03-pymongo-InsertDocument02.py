'''
Python MongoDB Insert Document

A document in MongoDB is the same as a record in SQL databases.


Return the _id Field

The insert_one() method returns a InsertOneResult object, which has a property, inserted_id, that holds the id of the inserted document.

'''
import pymongo

myclient = pymongo.MongoClient('mongodb://localhost:27017/')
mydb = myclient['w3schools-myDatabase']
mycollection = mydb["customers"]

mydict = { "name": "Peter", "address": "Lowstreet 27" }

x = mycollection.insert_one(mydict)

print(x.inserted_id)


