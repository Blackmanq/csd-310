from pymongo import MongoClient
connection = "mongodb+srv://admin:admin@cluster0.inz66kj.mongodb.net/pytech"
client = MongoClient(connection)
mydb = client.pytech
pytechdb = mydb["pytech"]
studentcollection = mydb.students


print("Student documents from find() query: \n")

for document in studentcollection.find():
    print(document)

result = studentcollection.update_one({"student_id": 1007}, {"$set": {"last_name": "Smith"}})

print("Displaying Student Document 1007")

for document in studentcollection.find({"student_id": 1007}):
    print(document)
