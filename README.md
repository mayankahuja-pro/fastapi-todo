```markdown
# 🚀 FastAPI Todo API

[![FastAPI](https://img.shields.io/badge/FastAPI-005571?style=for-the-badge&logo=fastapi)](https://fastapi.tiangolo.com/)
[![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)](https://www.python.org/)
[![SQLite](https://img.shields.io/badge/sqlite-%2307405e.svg?style=for-the-badge&logo=sqlite&logoColor=white)](https://www.sqlite.org/)
[![JWT](https://img.shields.io/badge/JWT-black?style=for-the-badge&logo=JSON%20web%20tokens)](https://jwt.io/)

A production-ready **RESTful API** designed for backend internship technical assessments. Demonstrates proficiency in **JWT Authentication**, **ORM Integration**, and **Scalable Project Architecture**. 
---

## ✨ Features

- 🔐 **Secure Auth**: JWT-based authentication with Bcrypt password hashing.
- 🏗 **Clean Architecture**: Separation of concerns (Models, Schemas, CRUD, Routes).
- 🛠 **Robust Validation**: Data integrity enforced via Pydantic.
- 📖 **Auto-Docs**: Interactive Swagger & ReDoc documentation.
- 🚦 **CRUD**: Full lifecycle management for Todo resources.

---

## 🛠 Tech Stack

| Component | Technology |
| :--- | :--- |
| **Framework** | FastAPI |
| **ORM** | SQLAlchemy |
| **Database** | SQLite (Development) |
| **Security** | Python-Jose (JWT), Passlib (Bcrypt) |
| **Server** | Uvicorn |

---

## 📂 Project Structure

```text
fastapi-todo/
├── app/
│   ├── auth.py          # JWT & Password logic
│   ├── crud.py          # Database abstraction layer
│   ├── database.py      # Engine & Session configuration
│   ├── main.py          # FastAPI entry point
│   ├── models.py        # SQLAlchemy database models
│   └── schemas.py       # Pydantic validation schemas
├── requirements.txt     # Dependency manifest
└── README.md            # Documentation
```

---

## 🚀 Getting Started

### 1. Setup Environment
```bash
# Clone & Enter
git clone https://github.com/your-username/fastapi-todo.git
cd fastapi-todo

# Virtual Env
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# Install
pip install -r requirements.txt
```

### 2. Launch Server
```bash
uvicorn app.main:app --reload
```
🔗 **API Portal:** [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

---

## 📑 API Reference

### Authentication
| Method | Endpoint | Description |
| :--- | :--- | :--- |
| `POST` | `/signup` | Create a new user account |
| `POST` | `/login` | Authenticate & receive Bearer Token |

### Todo Management
| Method | Endpoint | Description |
| :--- | :--- | :--- |
| `GET` | `/todos` | Retrieve all tasks for current user |
| `POST` | `/todos` | Create a new task |
| `PUT` | `/todos/{id}` | Update task status or content |
| `DELETE` | `/todos/{id}` | Remove a task |

---

## 🧠 Core Competencies Shown

- **Dependency Injection**: Managing database sessions and user state.
- **Middleware/Security**: Protecting routes using OAuth2 schemes.
- **Data Modeling**: Relational mapping between Users and Todos.
- **Error Handling**: Graceful API responses with proper HTTP status codes.

---

## 👨‍💻 Author

**Mayank Ahuja**  
 

---

## ⭐ Support

If this project helped you, please give it a **Star**!
```
