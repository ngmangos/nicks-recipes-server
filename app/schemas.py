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

class Recipe(BaseModel):
    id: str
    title: str

class RecipeCreate(BaseModel):
    title: str

class Session(BaseModel):
    user_id: str
    login_time: str
    session_id: str