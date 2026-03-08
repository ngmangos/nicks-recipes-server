from pydantic import BaseModel

class User(BaseModel):
    id: int
    name: str

class Recipe(BaseModel):
    id: int
    title: str

class RecipeCreate(BaseModel):
    title: str