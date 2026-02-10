from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from .database import Base, engine, SessionLocal
from . import models, schemas, crud, auth

# Saari database tables create kar rahe hain
Base.metadata.create_all(bind=engine)

app = FastAPI()

# Database session manage karne ke liye dependency
def get_db():
    db = SessionLocal() # Session open kiya
    try:
        yield db # Database connection use ke liye diya
    finally:
        db.close() # Kaam khatam hone par connection close kiya

# Signup route: Naya user register karne ke liye
@app.post("/signup")
def signup(user: schemas.UserCreate, db: Session = Depends(get_db)):
    return crud.create_user(db, user)

# Login route: Email aur Password check karke token dena
@app.post("/login")
def login(user: schemas.UserCreate, db: Session = Depends(get_db)):
    # Database me user check kar rahe hain
    db_user = db.query(models.User).filter(models.User.email == user.email).first()
    # Agar user nahi mila ya password galat hai to error bhejenge
    if not db_user or not auth.verify_password(user.password, db_user.password):
        raise HTTPException(status_code=401, detail="Invalid credentials")
    # Sahi hone par JWT token return karenge
    return {"access_token": auth.create_token(db_user.id)}

# Todo create karne ka route
@app.post("/todos")
def create(todo: schemas.TodoCreate, db: Session = Depends(get_db)):
    return crud.create_todo(db, todo.title, user_id=1)  # Abhi ke liye user_id 1 fix kiya hai

# Saare Todos dekhne ka route
@app.get("/todos")
def read_todos(db: Session = Depends(get_db)):
    return db.query(models.Todo).all()
