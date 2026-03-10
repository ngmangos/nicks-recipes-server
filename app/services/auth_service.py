from repositories.users import get_user, find_user
from repositories.sessions import store_session
from schemas import Session
from passlib.context import CryptContext
from datetime import datetime
import uuid

pwd_ctx = CryptContext(schemes=["bcrypt"], deprecated="auto")

def authenticate_user(email: str, password: str):
    user_id = find_user(email)
    if not user_id:
        return None
    user = get_user(user_id)
    if not user or not pwd_ctx.verify(password, user["password"]):
        return None
    
    session_id = str(uuid.uuid4())
    login_time = datetime.now()
    store_session(Session(session_id=session_id, user_id=user_id, login_time=login_time))
    return {"session_id": session_id}
