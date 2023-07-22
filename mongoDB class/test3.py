import pymongo

client = pymongo.MongoClient("mongodb+srv://kumaka6:Mani143K@cluster0.hnwdd5d.mongodb.net/?retryWrites=true&w=majority")
db = client.test
database = client['myinfo']
collection = database["kumaka"] #  collection name 'kumaka'


"""
#  requirement : to pull out all data
record = collection.find()
for i in record:
    print(i)
"""


"""
#  requirement : to pull out only 'company name'
record1 = collection.find({"companyName": "iNeuron"})
for i in record1:
    print(i)
"""


#  requirement : to pull out course offered is greater than 'E'
record2 = collection.find({"courseOffered": {"$gt":"E"}}) #  as per mongoDB $gt is 'greater than' and $gte - 'greater than equal to'
for i in record2:
    print(i)
