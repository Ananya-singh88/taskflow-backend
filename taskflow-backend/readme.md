# 🚀 TaskFlow — Secure Task Management Backend

## 📌 Overview
TaskFlow is a backend system that allows users to securely manage their tasks.  
It includes authentication, authorization, and full CRUD operations with user-specific data access.

---

## 🎯 Features

- User Signup & Login 🔐
- JWT Authentication (Secure Token System)
- Create Tasks 📝
- View Only Your Tasks 👀
- Update Tasks ✏️
- Delete Tasks ❌
- User-specific data protection (no access to others' tasks)

---

## 🧠 Tech Stack

- **Backend:** FastAPI
- **Database:** SQLite
- **ORM:** SQLAlchemy
- **Authentication:** JWT (python-jose)
- **API Testing:** Swagger UI

---

## ⚙️ How It Works

1. User signs up and logs in
2. System generates a JWT token
3. User sends requests with token
4. Backend verifies token
5. User can manage only their own tasks

---

## 🔗 API Endpoints

### Auth
- `POST /signup` → Register user
- `POST /login` → Login & get token

### Tasks
- `POST /tasks` → Create task
- `GET /tasks` → Get all user tasks
- `PUT /tasks/{task_id}` → Update task
- `DELETE /tasks/{task_id}` → Delete task

---

## 🔐 Authentication

Uses JWT (Bearer Token)

Example: 
---

## 🗄 Database Schema

### User
- id
- email (unique)
- password

### Task
- id
- title
- description
- owner_id (linked to user)

---

## 🚀 How to Run

```bash
git clone <your-repo-link>
cd taskflow-backend

python -m venv venv
venv\Scripts\activate

pip install -r requirements.txt

uvicorn main:app --reload