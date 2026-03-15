from pydantic import BaseModel

class Session(BaseModel):
    user_id: str
    login_time: str
    session_token: str

class LoginData(BaseModel):
    email: str
    password: str

class SessionToken(BaseModel):
    session_token: str