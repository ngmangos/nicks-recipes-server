from repositories.recipes import store_recipe, fetch_recipe
from schemas.recipes import RecipeCreate
import uuid

def create_recipe(recipe: RecipeCreate):
    recipe_id = str(uuid.uuid4())
    return store_recipe(Recipe(id=recipe_id, title=recipe.title))

def get_recipe(recipe_id: int):
    return fetch_recipe(recipe_id)