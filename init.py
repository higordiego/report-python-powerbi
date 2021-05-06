# import pandas as pd
import pymongo
import certifi

client = pymongo.MongoClient("mongodb+srv://teste:juniorgl5@ufe.wjqgv.mongodb.net/", tlsCAFile=certifi.where())
db = client['test']

a = db['dashboard'].find_one()
print(a)
