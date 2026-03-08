from fastapi import APIRouter
from schemas import User
from services.user_service import create_user, get_users

router = APIRouter()

@router.get("/{user_id}")
def read_user(user_id: int):
    return {"user_id": user_id}

@router.put("/{user_id}")
def update_user(user_id: int, user: User):
    return {"user_name": user.name, "user_id": user_id}