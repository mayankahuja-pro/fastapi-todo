from pydantic import BaseModel

# User banate waqt kaunsi fields chahiye (Signup/Login ke liye)
class UserCreate(BaseModel):
    email: str
    password: str

# Todo banate waqt sirf title mangenge
class TodoCreate(BaseModel):
    title: str

# Database se data bhejte waqt ye format use hoga
class TodoOut(BaseModel):
    id: int
    title: str
    completed: bool

    class Config:
        from_attributes = True # ORM objects (SQLAlchemy) ko Pydantic models me convert karne ke liye
