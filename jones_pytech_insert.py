from pymongo import MongoClient
connection = "mongodb+srv://admin:admin@cluster0.inz66kj.mongodb.net/?retryWrites=true&w=majority"
client = MongoClient(connection)
mydb = client.pytech
pytechdb = mydb["pytech"]
studentcollection = mydb.students

student1 = {"first_name": "Quincy", "last_name": "Jones", "student_id": 1007}
student2 = {"first_name": "Sean", "last_name": "Hardge", "student_id": 1008}
student3 = {"first_name": "Haydn", "last_name": "Hurst", "student_id": 1009}

student1_student_id = studentcollection.insert_one(student1).inserted_id
student2_student_id = studentcollection.insert_one(student2).inserted_id
student3_student_id = studentcollection.insert_one(student3).inserted_id

print("Student 1 has been added to the students collection with document_id" + str(student1_student_id))
print("Student 2 has been added to the students collection with document_id" + str(student2_student_id))
print("Student 3 has been added to the students collection with document_id" + str(student3_student_id))
