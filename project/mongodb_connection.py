from pymongo import MongoClient

db_url = "mongodb://pschome.iptime.org:27017"

def insert_db(item_list):
  client = MongoClient(db_url)
  db = client["crawling_project"]
  collection = db["products"]
  collection.insert_many(item_list)
  client.close()
  
def get_db(pipeline):
  client = MongoClient(db_url)
  db = client["crawling_project"]
  if pipeline == None or pipeline == []:
    documents = db["products"].find()
  else:
    documents = db["products"].aggregate(pipeline)
    
  for document in documents:
    print(document)
    
  client.close()

