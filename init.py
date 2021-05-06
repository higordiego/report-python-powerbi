# import pandas as pd
import pymongo
import certifi

client = pymongo.MongoClient("sua_url_aqui", tlsCAFile=certifi.where())
db = client['test']

a = db['dashboard'].find_one()
print(a)
