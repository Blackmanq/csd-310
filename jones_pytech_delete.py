from pymongo import MongoClient
connection = "mongodb+srv://admin:admin@cluster0.inz66kj.mongodb.net/pytech"
client = MongoClient(connection)
mydb = client.pytech
pytechdb = mydb["pytech"]
studentcollection = mydb.students


print("Student documents from find() query: \n")

for document in studentcollection.find():
    print(document)
print()

student4 = {"first_name": "James", "last_name": "Jones", "student_id": 1010}
student4_student_id = studentcollection.insert_one(student4).inserted_id

print("--Insert Statements--")
print("Inserted student record into the students collection with document_id: 632935cb74465d92a7be671b \n")

print("--Displaying Student Test Doc--")
print()

for document in studentcollection.find({"student_id": 1010}):
    print(document)

studentcollection.delete_one({"student_id": 1010})

print()
print("Student documents from find() query: \n")

for document in studentcollection.find():
    print(document)

