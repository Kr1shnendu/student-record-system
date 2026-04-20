# 🎓 Student Record System

A full-stack **Student Record Management System** built using **Flask** and **MongoDB**.
This project provides both:

- 🌐 **Web UI (Templates using Flask Jinja2)**
- 🔗 **REST API (JSON-based CRUD operations)**

---

## Features

### 🌐 Web Interface

- Add new student records
- View all students
- Update student details
- Delete student records
- Simple UI using HTML templates

### 🔗 REST API

- Create student (POST)
- Get all students (GET)
- Update student (PUT)
- Delete student (DELETE)
- JSON-based request & response

---

## 📁 Project Structure

```
STUDENT-RECORD-SYSTEM/
│
├── static/
│   └── style.css
│
├── templates/
│   ├── index.html
│   ├── create.html
│   ├── students.html
│   └── update.html
│
├── app.py          # Web UI (Flask + Templates)
├── server.py       # REST API (JSON-based)
├── requirements.txt
```

---

## 🛠️ Tech Stack

- **Backend:** Flask
- **Database:** MongoDB Atlas
- **Frontend:** HTML, CSS (Jinja2 Templates)
- **Driver:** PyMongo

---

## ⚙️ Installation & Setup

### 1️⃣ Clone the Repository

```bash
git clone <your-repo-url>
cd STUDENT-RECORD-SYSTEM
```

### 2️⃣ Create Virtual Environment (Optional but Recommended)

```bash
python -m venv venv
source venv/bin/activate     # Linux/Mac
venv\Scripts\activate        # Windows
```

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 🔐 MongoDB Configuration

Update your MongoDB connection string in both `app.py` and `server.py`:

```python
MongoClient("your_mongodb_connection_string")
```

⚠️ **Important:** Never expose credentials in public repositories. Use environment variables instead.

---

## ▶️ Running the Project

### 🌐 Run Web Application

```bash
python app.py
```

Visit:
👉 [http://127.0.0.1:5000/](http://127.0.0.1:5000/)

---

### 🔗 Run API Server

```bash
python server.py
```

---

## 📡 API Endpoints

### ➕ Create Student

```
POST /students/create
```

```json
{
  "name": "John",
  "marks": "85",
  "course": "CS"
}
```

---

### 📄 Get All Students

```
GET /students/all
```

---

### ✏️ Update Student

```
PUT /students/update
```

```json
{
  "id": "student_id",
  "name": "Updated Name",
  "marks": "90",
  "course": "IT"
}
```

---

### ❌ Delete Student

```
DELETE /students/delete
```

```json
{
  "id": "student_id"
}
```

---

## 📌 Notes

- `app.py` → Handles UI and form-based operations
- `server.py` → Handles API (JSON-based requests)
- Both connect to the same MongoDB collection
- Uses `ObjectId` for MongoDB document identification

---

## 💡 Future Improvements

- Add authentication (JWT / login system)
- Input validation & error handling
- Pagination for student list
- Search & filter functionality
- Docker deployment

---

## 👨‍💻 Author

**Krishnendu Maji**
