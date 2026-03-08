from pydantic import BaseModel

class User(BaseModel):
    id: str
    name: str

class Recipe(BaseModel):
    id: str
    title: str

class RecipeCreate(BaseModel):
    title: str