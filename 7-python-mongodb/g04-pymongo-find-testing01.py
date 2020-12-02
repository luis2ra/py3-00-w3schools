import pymongo
from files.phone import Phone

myclient = pymongo.MongoClient('mongodb://localhost:27017/')
mydb = myclient['movatec_system']
mycollection = mydb["phones"]


phones_dist = mycollection.distinct('debtor_id')
    
phones_dict = {}
for reg in phones_dist:
    phones_dict[reg] = list(mycollection.find( {'debtor_id' : reg }, { '_id':0, 'debtor_ida':0 } ))


print('--->', phones_dist)
print('\n')
print('--->', phones_dict)