#  TaskFlow Pro — Full Stack Task Management System

TaskFlow Pro is a full-stack task management application built with a hybrid backend architecture using FastAPI, Django, and React. It demonstrates secure authentication, RESTful API design, and real-world frontend-backend integration.

---

##  Features

-  JWT-based authentication (login & signup)
-  Create, view, and delete tasks (CRUD operations)
-  User-specific task isolation (each user sees only their data)
-  FastAPI backend for high-performance APIs
-  Django Admin panel for backend data management
-  React frontend with protected routes
-  Full end-to-end data flow (UI → API → Database)

---

## Tech Stack

- **Backend:** FastAPI, SQLAlchemy
- **Frontend:** React (Axios for API calls)
- **Admin Panel:** Django
- **Database:** SQLite
- **Authentication:** JWT (JSON Web Tokens)

---

## Architecture


---

##  Key Highlights

- Built using **5+ technologies** in a **3-tier architecture**
- Developed **6+ RESTful APIs** for authentication and task management
- Secured **100% protected routes using JWT authentication**
- Achieved **~8ms API response time (0.0083s)** for task retrieval
- Implemented **user-task relationship with complete data isolation**

---

##  Setup Instructions

### Clone the repository

```bash
git clone https://github.com/Ananya-singh88/taskflow-backend.git
cd taskflow-backend

python -m venv venv
venv\Scripts\activate   # Windows
pip install -r requirements.txt

uvicorn main:app --reload
Runs on: http://127.0.0.1:8000

3️ Frontend Setup (React)
cd frontend
npm install
npm start

Runs on: http://localhost:3000

4️ Django Admin Setup
cd admin_panel
python manage.py runserver 8001

Runs on: http://127.0.0.1:8001/admin
