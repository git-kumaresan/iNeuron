import pymongo
from pymongo import MongoClient
import urllib.parse

data = {
    "name" : "kumaresan",
    "mail_id": "kumaka@ai",
    "subject": ["data science", "Big data", "data analytics"]
}

username = urllib.parse.quote_plus('kumaka6')
password = urllib.parse.quote_plus("Mani143K")

url = "mongodb+srv://{}:{}@cluster0.hnwdd5d.mongodb.net/?retryWrites=true&w=majority".format(username, password)

client = MongoClient(url)
db = client['mydatabase']
collection = db['mycollection']
collection.insert_one(data)



"""
client = MongoClient("mongodb+srv://kumaka6:Mani%40K@cluster0.hnwdd5d.mongodb.net/?retryWrites=true&w=majority")

db = client['mydatabase']
collection = db['mycollection']
collection.insert_one(data)
"""

