```md
# FastAPI Todo API 🚀

A beginner-friendly **FastAPI backend project** built to demonstrate **REST API development, JWT authentication, and database integration** using SQLAlchemy.  
This project is designed specifically for **backend internship interviews**.

---

## 🛠 Tech Stack

- **FastAPI** – Web framework
- **SQLAlchemy** – ORM
- **SQLite** – Database
- **Pydantic** – Data validation
- **JWT (python-jose)** – Authentication
- **Passlib (bcrypt)** – Password hashing
- **Uvicorn** – ASGI server

---

## 📁 Project Structure

```

fastapi-todo/
│
├── app/
│   ├── main.py        # Application entry point
│   ├── database.py    # Database configuration
│   ├── models.py      # SQLAlchemy models
│   ├── schemas.py     # Pydantic schemas
│   ├── auth.py        # Authentication & JWT logic
│   ├── crud.py        # Database operations
│
├── requirements.txt
└── README.md

````

---

## ⚙️ Installation & Setup

### 1️⃣ Clone the repository
```bash
git clone https://github.com/your-username/fastapi-todo.git
cd fastapi-todo
````

### 2️⃣ Create virtual environment

```bash
python -m venv venv
source venv/bin/activate   # Windows: venv\Scripts\activate
```

### 3️⃣ Install dependencies

```bash
pip install -r requirements.txt
```

---

## ▶️ Run the Application

```bash
uvicorn app.main:app --reload
```

Server will start at:

```
http://127.0.0.1:8000
```

---

## 📖 API Documentation

FastAPI provides interactive API docs automatically:

* **Swagger UI** → [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
* **ReDoc** → [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)

---

## 🔐 Authentication Flow (JWT)

1. User signs up with email and password
2. Password is securely hashed using bcrypt
3. User logs in and receives a JWT access token
4. Token is used to access protected endpoints

---

## 🔗 API Endpoints

### 🔹 Auth

| Method | Endpoint  | Description           |
| ------ | --------- | --------------------- |
| POST   | `/signup` | Register new user     |
| POST   | `/login`  | Login & get JWT token |

### 🔹 Todos

| Method | Endpoint      | Description        |
| ------ | ------------- | ------------------ |
| POST   | `/todos`      | Create a todo      |
| GET    | `/todos`      | Get all user todos |
| PUT    | `/todos/{id}` | Update todo        |
| DELETE | `/todos/{id}` | Delete todo        |

---

## 🧠 Key Concepts Demonstrated

* RESTful API design
* Dependency Injection (`Depends`)
* JWT-based authentication
* Password hashing
* ORM vs raw SQL
* Pydantic schema validation
* Clean project structure

---

## 🎯 Why This Project?

This project was built to:

* Practice **backend fundamentals**
* Understand **FastAPI architecture**
* Prepare for **backend internship interviews**

---

## 🚀 Future Improvements

* Role-based access control
* Refresh tokens
* Pagination & filtering
* Docker support
* Deployment (Render / Fly.io)

---

## 👨‍💻 Author

**Your Name**
Backend Developer | FastAPI Enthusiast

📌 *This project is part of my backend internship preparation.*

---

## ⭐ If you like this project

Give it a ⭐ and feel free to fork or contribute!

```

If you want, I can:
- Tailor this README to **your exact code**
- Write a **strong resume bullet**
- Help you answer **“Explain your project”** perfectly for interview

Just say the word 🔥
```
