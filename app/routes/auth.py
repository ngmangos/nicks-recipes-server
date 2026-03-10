from fastapi import APIRouter
from schemas import User, UserCreate
from services.auth_service import authenticate_user

router = APIRouter()

@router.post("/login")
def login_user(email: str, password: str):
    return authenticate_user(email, password)

@router.post("/logout")
def logout_user(session_id: str):
    return {"message": "User logged out successfully"}