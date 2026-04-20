from flask import Flask, request
from pymongo import MongoClient
from bson import ObjectId

client = MongoClient("mongodb+srv://Krishnendu:krish@cluster0.77hdsjw.mongodb.net/?appName=Cluster0")
db = client["student_records"]
collection = db["students"]

app = Flask(__name__)


@app.route("/")
def home():
    return "Welcome to Student Record System!!!"

@app.route("/students/create", methods = ["POST"])
def create_student():
    data = request.json
    student = {
        "name": data["name"],
        "marks": data["marks"],
        "course": data["course"]
    }
    result = collection.insert_one(student)
    return {
        "status": 201,
        "message": "Student created",
        "id": str(result.inserted_id)
    }


@app.route("/students/all", methods=["GET"])
def get_students():
    students = []
    data = collection.find()
    for student in data:
        students.append({
            "id": str(student["_id"]),
            "name": student["name"],
            "marks": student["marks"],
            "course": student["course"]
        })
    return {
        "status": 200,
        "data": students
    }


@app.route("/students/update", methods=["PUT"])
def update_student():
    data = request.json
    result = collection.update_one(
        {"_id": ObjectId(data["id"])},
        {
            "$set": {
                "name": data["name"],
                "marks": data["marks"],
                "course": data["course"]
            }
        })
        
    return {
        "status": 202,
        "message": "Updated successfully",
        "id": data["id"]
    }


@app.route("/students/delete", methods=["DELETE"])
def delete_student():
    data = request.json

    result = collection.delete_one({
        "_id": ObjectId(data["id"])
    })

    return {
        "status": 205,
        "message": "Student deleted successfully",
        "id": data["id"]
    }

if __name__ == "__main__":
    app.run(debug=True)
