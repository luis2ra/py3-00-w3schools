'''
Check if Collection Exists

Remember: In MongoDB, a collection is not created until it gets content, so if this is your first time creating a collection, you should complete the next chapter (create document) before you check if the collection exists!

'''
import pymongo

myclient = pymongo.MongoClient('mongodb://localhost:27017/')

mydb = myclient['w3schools-myDatabase']

collectionlist = mydb["customers"]

# Return a list of all collections in your database:
print(mydb.list_collection_names())
