from fastapi import APIRouter
from schemas.users import User, UserCreate
from services.user_service import create_user, get_user_by_id

router = APIRouter()

@router.post("/")
def register_user(user: UserCreate):
    return create_user(user)

@router.get("/{user_id}")
def get_user(user_id: str):
    return get_user_by_id(user_id)