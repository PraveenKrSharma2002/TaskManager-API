# 🚀 Task Management API (Flask + JWT)

A production-like Task Management REST API built using Flask with JWT authentication.  
This API allows users to securely manage tasks with role-based access, pagination, and filtering.

---

## ✨ Features

- 🔐 User Authentication (JWT)
- 📋 CRUD Operations on Tasks
- 👤 Assign Tasks to Users
- 🛡️ Role-Based Access Control (Admin/User)
- 📄 Pagination & Filtering
- 🧪 Unit Testing (unittest)

---

## 🛠️ Tech Stack

- Python (Flask)
- SQLAlchemy (ORM)
- Flask-JWT-Extended
- SQLite (Database)

---

## ⚙️ Setup & Installation

### 1️⃣ Clone the Repository
```bash
git clone <repo-url>
cd TaskManager

2️⃣ Create Virtual Environment
python -m venv venv

3️⃣ Activate Virtual Environment

Windows:
venv\Scripts\activate

Mac/Linux:
source venv/bin/activate

4️⃣ Install Dependencies
pip install -r requirements.txt

5️⃣ Run the Application
python run.py

👉 Server will start at:

http://127.0.0.1:5000
🔗 API Endpoints
Method	Endpoint	Description
POST	/register	Register new user
POST	/login	Login & get JWT token
POST	/add	Add new task
GET	/tasks	Get tasks (pagination + filtering)
PUT	/update/<id>	Update task
DELETE	/delete/<id>	Delete task

🔐 Authentication
All protected routes require a JWT token.

👉 Add token in request header:
Authorization: Bearer <your_token>

🧪 Running Tests
python -m unittest discover

📌 Example Request
Add Task
{
  "title": "Complete assignment"
}

🎯 Project Highlights
Secure API using JWT authentication
Clean and modular code structure
Implements real-world backend concepts
Ready for production-level extension

👨‍💻 Author
Praveen Kumar Sharma