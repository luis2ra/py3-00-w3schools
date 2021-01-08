import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["w3schools-myDatabase"]
mycol = mydb["customers"]

# Return all documents in the "customers" collection, and print each document:
for x in mycol.find():
    print(x)
    
# myquery = {}
# newvalues = { "$set": { "organization_id": "" } }

# x = mycol.update_many(myquery, newvalues)

# print(x.modified_count, "documents updated of ", mycol.name)

# Return all documents in the "customers" collection, and print each document:
for y in mycol.find():
    if y['organization_id'] == '':
        print('esta vacio')
        z = mycol.find_one({}, { "_id": 1, "name": 1, "organization_id": 1 })
        print(z)
        if z["name"] == "Minnie":
            myquery = { "_id": z["_id"] }
            newvalues = { "$set": { "organization_id": "123" } }
            mycol.update_one(myquery, newvalues)
    else:
        print('tiene un valor')