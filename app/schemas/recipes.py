from pydantic import BaseModel

class Recipe(BaseModel):
    id: str
    title: str

class RecipeCreate(BaseModel):
    title: str