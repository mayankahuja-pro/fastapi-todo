from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from .database import Base

# User table define kar rahe hain
class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True) # Unique ID har user ke liye
    email = Column(String, unique=True, index=True) # User ka email (unique hona chahiye)
    password = Column(String) # Hashed password store karne ke liye

# Todo table define kar rahe hain
class Todo(Base):
    __tablename__ = "todos"

    id = Column(Integer, primary_key=True)
    title = Column(String) # Todo ka naam ya title
    completed = Column(Boolean, default=False) # Status: task khatam hua ya nahi
    owner_id = Column(Integer, ForeignKey("users.id")) # Batata hai ki ye todo kis user ka hai
