from repositories.users import store_new_user, get_user, find_user
from schemas import UserCreate, User
from passlib.context import CryptContext
import uuid

pwd_ctx = CryptContext(schemes=["bcrypt"], deprecated="auto")

def create_user(user: UserCreate):
    if find_user(user.email):
        raise ValueError("Email already registered")
    hashed = pwd_ctx.hash(user.password)
    user_id = str(uuid.uuid4())
    return {"user_id": store_new_user(User(id=user_id, name=user.name, email=user.email, password=hashed))}

def get_user_by_id(user_id: str):
    return get_user(user_id)