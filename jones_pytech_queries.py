from pymongo import MongoClient
connection = "mongodb+srv://admin:admin@cluster0.inz66kj.mongodb.net/pytech"
client = MongoClient(connection)
mydb = client.pytech
pytechdb = mydb["pytech"]
studentcollection = mydb.students

print("Student documents from find() query: \n")

for document in studentcollection.find():
    print(document)
    
