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

## 1️⃣ Clone the Repository

git clone https://github.com/PraveenKrSharma2002/TaskManager-API.git
cd TaskManager

## 2️⃣ Create Virtual Environment

python -m venv venv

## 3️⃣ Activate Virtual Environment

Windows: venv\Scripts\activate

## 4️⃣ Install Dependencies

pip install -r requirements.txt

## 5️⃣ Run the Application

python run.py

---

👉 Server will start at:
http://127.0.0.1:5000

## 🔗 API Endpoints
<img width="762" height="385" alt="image" src="https://github.com/user-attachments/assets/14c2669c-3ced-4a02-a6df-b4e004ebfbce" />

🔐 Authentication

All protected routes require a JWT token.

👉 Add token in request header: Authorization: Bearer <your_token>

## 🧪 Running Tests

python -m unittest discover

---

## 🎯 Project Highlights

-Secure API using JWT authentication

-Clean and modular code structure

-Implements real-world backend concepts

-Ready for production-level extension

---
## 👨‍💻 Author

Praveen Kumar Sharma
