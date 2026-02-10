from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# Database ki file kahan save hogi, uska path (SQLite use kar rahe hain)
DATABASE_URL = "sqlite:///./todo.db"

# Engine create kar rahe hain jo database se interact karega
# connect_args={"check_same_thread": False} SQLite ke liye zaroori hai
engine = create_engine(
    DATABASE_URL, connect_args={"check_same_thread": False}
)

# SessionLocal class banayi hai, isse hum database me changes (read/write) karenge
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base class banayi hai, isi ko inherit karke hum models (tables) banayenge
Base = declarative_base()
