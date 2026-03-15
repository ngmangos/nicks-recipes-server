from repositories.users import store_new_user, get_user, find_user
from schemas.users import UserCreate, User
from passlib.context import CryptContext
import uuid
from fastapi import HTTPException, status

pwd_ctx = CryptContext(schemes=["bcrypt"], deprecated="auto")

def create_user(user: UserCreate):
    if find_user(user.email):
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="Email is already registered"
        )
    hashed = pwd_ctx.hash(user.password)
    user_id = str(uuid.uuid4())
    return {"user_id": store_new_user(User(id=user_id, name=user.name, email=user.email, password=hashed))}

def get_user_by_id(user_id: str):
    user = get_user(user_id)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found"
        )
    return user