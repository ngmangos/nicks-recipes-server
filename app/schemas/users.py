from pydantic import BaseModel

class User(BaseModel):
    id: str
    name: str
    email: str
    password: str

class UserCreate(BaseModel):
    name: str
    email: str
    password: str