data =  [
        {
            "item": "canvas",
            "qty": 100,
            "size": {"h": 28, "w": 35.5, "uom": "cm"},
            "status": "A",
        },
        {
            "item": "journal",
            "qty": 25,
            "size": {"h": 14, "w": 21, "uom": "cm"},
            "status": "A",
        },
        {
            "item": "mat",
            "qty": 85,
            "size": {"h": 27.9, "w": 35.5, "uom": "cm"},
            "status": "A",
        },
        {
            "item": "mousepad",
            "qty": 25,
            "size": {"h": 19, "w": 22.85, "uom": "cm"},
            "status": "P",
        },
        {
            "item": "notebook",
            "qty": 50,
            "size": {"h": 8.5, "w": 11, "uom": "in"},
            "status": "P",
        },
        {
            "item": "paper",
            "qty": 100,
            "size": {"h": 8.5, "w": 11, "uom": "in"},
            "status": "D",
        },
        {
            "item": "planner",
            "qty": 75,
            "size": {"h": 22.85, "w": 30, "uom": "cm"},
            "status": "D",
        },
        {
            "item": "postcard",
            "qty": 45,
            "size": {"h": 10, "w": 15.25, "uom": "cm"},
            "status": "A",
        },
        {
            "item": "sketchbook",
            "qty": 80,
            "size": {"h": 14, "w": 21, "uom": "cm"},
            "status": "A",
        },
        {
            "item": "sketch pad",
            "qty": 95,
            "size": {"h": 22.85, "w": 30.5, "uom": "cm"},
            "status": "A",
        },
    ]

import pymongo

client = pymongo.MongoClient("mongodb+srv://kumaka6:Mani143K@cluster0.hnwdd5d.mongodb.net/?retryWrites=true&w=majority")
db = client.test
database = client['inventory']
collection = database["table"]
#  collection.insert_many(data)

"""
##  to view data
record = collection.find()
for i in record:
    print(i)
"""

#  fileter operations
#  filterdata = collection.find({'status':'A'})  #  finding all data status = A
#  filterdata = collection.find({'status':{'$in': ['A', 'P']}})  #  finding all data either status = A or P; $in is inbuild keyword in mongoDB
#  filterdata = collection.find({'status': {'$gt' : 'B'}})   #  finding all data where status greater than 'B'
#  filterdata = collection.find({'qty': {'$gte' : 80}})
#  filterdata = collection.find({'item': 'sketch pad'} and {'qty' : 95})
#  filterdata = collection.find({'item': 'sketch pad'} and {'qty' : {'$gte' : 75}})
#  filterdata = collection.find({'item': 'sketch pad' , 'qty' : {'$gte' : 75}})
#  filterdata = collection.find({'$or': [ {'item': 'sketch pad'},{'qty': {'$gte': 100}}]})  # OR condition

"""
filterdata = collection.find({'$or': [ {'item': 'sketch pad'},{'qty': {'$gte': 100}}]})  # OR condition
for i in filterdata:
    print(i)
"""

#  to perform update operation
# update_one and update_many
"""
collection.update_one({'item': 'canvas'}, {"$set": {'item': 'Kumar'}})
d= collection.find({'item': 'Kumar'})
for i in d:
    print(i)
"""

#  deleting record
collection.delete_one({'item': 'Kumar'})  # deleing record one at a time
d= collection.find({'item': 'Kumar'})
for i in d:
    print(i)

#  on MongoDB, using filter option, we can view result as per requiremnet ;
#  {'item':'Kumar'}
#  {'qty' : {'$gte' :85}}

# Image database on MongoDB ?, convert into Base64 , then possible.
#