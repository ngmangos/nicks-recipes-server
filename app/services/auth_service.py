from repositories.users import get_user, find_user
from repositories.sessions import store_session
from schemas.auth import Session
from passlib.context import CryptContext
from datetime import datetime
import uuid
from fastapi import HTTPException, status

pwd_ctx = CryptContext(schemes=["bcrypt"], deprecated="auto")

def authenticate_user(email: str, password: str):
    user_id = find_user(email)
    if not user_id:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid email or password"
        )
    user = get_user(user_id)
    if not user or not pwd_ctx.verify(password, user["password"]):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, 
            detail="Invalid email or password"
        )
    
    session_token = str(uuid.uuid4())
    login_time = datetime.now().isoformat()
    store_session(
        Session(
            session_token=session_token,
            user_id=user_id,
            login_time=login_time
        )
    )
    return {"session_token": session_token}
