'''
Python MongoDB Find

* In MongoDB we use the find and findOne methods to find data in a collection.
* Just like the SELECT statement is used to find data in a table in a MySQL database.


Return Only Some Fields

The second parameter of the find() method is an object describing which fields to include in the result.
This parameter is optional, and if omitted, all fields will be included in the result.

'''
import pymongo

myclient = pymongo.MongoClient('mongodb://localhost:27017/')
mydb = myclient['w3schools-myDatabase']
mycollection = mydb["customers"]

# Return only the names and addresses, not the _ids:
for x in mycollection.find({},{ "_id": 0, "name": 1, "address": 1 }):
    print(x)

    
for x in mycollection.find({},{ "_id": 1, "name": 1, "organization_id": 1 }):
    if x["name"] == "Minnie":
        print(x["name"])
        x["organization_id"] = "123"
    else:
        print('false')
    
    
