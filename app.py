from flask import Flask, render_template, request, redirect, url_for
from pymongo import MongoClient
from bson import ObjectId

client = MongoClient("mongodb+srv://Krishnendu:krish@cluster0.77hdsjw.mongodb.net/?appName=Cluster0")
db = client["student_records"]
collection = db["students"]

app = Flask(__name__)

@app.route("/")
def home_page():
    return render_template("index.html")

@app.route("/create")
def create_page():
    return render_template("create.html")

@app.route('/update', methods=['POST'])
def update():
    student_id = request.form.get("student_id")
    return render_template("update.html", student_id=student_id)

@app.route('/delete', methods=['POST'])
def delete():
    student_id = request.form.get("student_id")
    return f"Deleting student with ID: {student_id}"



@app.route("/api/students/create", methods=["POST"])
def create_student():
    student = {
        "name": request.form["name"],
        "marks": request.form["marks"],
        "course": request.form["course"]
    }

    collection.insert_one(student)

    return render_template("success.html", message="Added Successfully...")


@app.route("/students/all")
def get_students():
    students = []

    for s in collection.find():
        students.append({
            "id": str(s["_id"]),
            "name": s["name"],
            "marks": s["marks"],
            "course": s["course"]
        })

    return render_template("students.html", students=students)


@app.route("/api/students/update/<id>", methods=["POST"])
def update_student(id):
    collection.update_one(
        {"_id": ObjectId(id)},
        {
            "$set": {
                "name": request.form["name"],
                "marks": request.form["marks"],
                "course": request.form["course"]
            }
        }
    )
    return redirect(url_for("get_students"))


@app.route("/api/students/delete/<id>", methods=["POST"])
def delete_student(id):
    collection.delete_one({"_id": ObjectId(id)})
    return redirect(url_for("get_students"))



if __name__ == "__main__":
    app.run(debug=True)