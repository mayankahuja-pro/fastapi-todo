import bcrypt
from jose import jwt
from datetime import datetime, timedelta

# JWT Token ke liye secret key aur algorithm
SECRET_KEY = "secret123"
ALGORITHM = "HS256"

# Password ko hash karne ka function (security ke liye)
def hash_password(password: str):
    # Password ko bytes me convert kar rahe hain aur 72 characters tak limit kar rahe hain
    pwd_bytes = password.encode('utf-8')[:72]
    # Salt generate karke password ko hash kar rahe hain
    salt = bcrypt.gensalt()
    return bcrypt.hashpw(pwd_bytes, salt).decode('utf-8')

# Password sahi hai ya nahi, check karne ka function
def verify_password(password: str, hashed: str):
    pwd_bytes = password.encode('utf-8')[:72]
    # Input password aur database wala hash compare kar rahe hain
    return bcrypt.checkpw(pwd_bytes, hashed.encode('utf-8'))

# Login ke baad ek temporary token create karne ke liye
def create_token(user_id: int):
    payload = {
        "sub": user_id, # User ki ID store kar rahe hain
        "exp": datetime.utcnow() + timedelta(hours=1) # Token 1 ghante me expire ho jayega
    }
    return jwt.encode(payload, SECRET_KEY, algorithm=ALGORITHM)
