from repositories.recipes import save_recipe, fetch_recipe
from schemas import RecipeCreate

def create_recipe(recipe: RecipeCreate):
    return save_recipe(recipe)

def get_recipe(recipe_id: int):
    return fetch_recipe(recipe_id)