from utils.json_store import load_data, save_data
from schemas.recipes import Recipe

FILE = "data/recipes.json"

def fetch_recipe(recipe_id: str):
    recipes = load_data(FILE)
    return recipes.get(str(recipe_id), None)

def store_recipe(recipe: Recipe):
    recipes = load_data(FILE)
    recipes[recipe.id] = recipe.dict()
    save_data(FILE, recipes)
    return recipe.id