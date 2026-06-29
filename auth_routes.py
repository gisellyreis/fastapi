from fastapi import APIRouter, Depends, HTTPException
from models import User
from dependencies import get_db_session
from main import bcrypt_context

auth_router = APIRouter(prefix="/auth", tags=["auth"])

@auth_router.get("/")
async def auth_root():
    """Authentication endpoint"""
    return {"message": "Authentication endpoint"}

@auth_router.post("/signup")
async def signup(email: str, password: str, name: str, session = Depends(get_db_session)):
    user = session.query(User).filter(User.email == email).first()
    if user:
        raise HTTPException(status_code=400, detail="Email already registered")
    else:
        crypted_password = bcrypt_context.hash(password)
        new_user = User(name, email, crypted_password)
        session.add(new_user)
        session.commit()
        return {"message": "User created successfully"}