from fastapi import APIRouter
from services.auth_service import authenticate_user
from schemas.auth import SessionToken, LoginData

router = APIRouter()

@router.post("/login")
def login_user( login_data: LoginData):
    return authenticate_user(login_data.email, login_data.password)

@router.post("/logout")
def logout_user(session_token: SessionToken):
    return {"message": "User logged out successfully"}