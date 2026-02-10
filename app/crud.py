from .models import User, Todo
from .auth import hash_password

# Naya user banane ka function
def create_user(db, user):
    db_user = User(
        email=user.email,
        password=hash_password(user.password) # Password hash karke save kar rahe hain
    )
    db.add(db_user) # Database me add kiya
    db.commit() # Changes save kiye
    db.refresh(db_user) # Naye user ka data (jaise ID) wapas laya
    return db_user

# Naya Todo banane ka function
def create_todo(db, title, user_id):
    todo = Todo(title=title, owner_id=user_id)
    db.add(todo)
    db.commit()
    db.refresh(todo)
    return todo
