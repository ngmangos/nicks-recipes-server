from fastapi import APIRouter
from schemas import Recipe, RecipeCreate
from services.recipe_service import create_recipe, get_recipe

router = APIRouter()

@router.post("/")
def create_new_recipe(recipe: RecipeCreate):
    return create_recipe(recipe)

@router.get("/{recipe_id}")
def read_recipe(recipe_id: int):
    return get_recipe(recipe_id)