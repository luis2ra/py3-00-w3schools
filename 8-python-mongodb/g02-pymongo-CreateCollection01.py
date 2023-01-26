'''
Python MongoDB Create Collection

A collection in MongoDB is the same as a table in SQL databases.


Creating a Collection

* To create a collection in MongoDB, use database object and specify the name of the collection you want to create.

* MongoDB will create the collection if it does not exist.

'''

import pymongo

myclient = pymongo.MongoClient('mongodb://localhost:27017/')

mydb = myclient['w3schools-myDatabase']

mycollection = mydb["customers"]

# collection created!
