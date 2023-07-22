
import pymongo

#  establishing connecting with MongoDB
client = pymongo.MongoClient("mongodb+srv://kumaka6:Mani143K@cluster0.hnwdd5d.mongodb.net/?retryWrites=true&w=majority")
db = client.test

list_of_records = [
    {'companyName': 'iNeuron',
     'product': 'Affordable AI',
     'courseOffered': 'Machine Learning with Deployment'},

    {'companyName': 'iNeuron',
     'product': 'Affordable AI',
     'courseOffered': 'Deep Learning for NLP and Computer vision'},

    {'companyName': 'iNeuron',
     'product': 'Master Program',
     'courseOffered': 'Data Science Masters Program'}
]

database = client['myinfo']
collection = database["kumaka"] #  collection name 'kumaka'
collection.insert_many(list_of_records)


