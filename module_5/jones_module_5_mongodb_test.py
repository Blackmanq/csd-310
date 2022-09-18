from pymongo import MongoClient
connection = MongoClient("mongodb+srv://admin:admin@cluster0.inz66kj.mongodb.net/pytech")
pytechdb = connection["pytech"]
studentcollection = pytechdb["students"]

print("-- pytech Collection List --")
print(["students"])
