import pymongo

#  establishing connecting with MongoDB
client = pymongo.MongoClient("mongodb+srv://kumaka6:Mani143K@cluster0.hnwdd5d.mongodb.net/?retryWrites=true&w=majority")
db = client.test

data = {
    "name" : "kumaresan",
    "mail_id": "kumaka@ai",
    "subject": ["data science", "Big data", "data analytics"]
}

database = client['myinfo']
collection = database["kumaka"] #  collection name 'kumaka'
collection.insert_one(data)

