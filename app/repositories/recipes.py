from utils.json_store import load_data, save_data
from schemas import RecipeCreate, Recipe
import uuid

FILE = "recipes.json"

def fetch_recipe(recipe_id: str):
    recipes = load_data(FILE)
    return recipes.get(str(recipe_id), None)

def save_new_recipe(recipe: RecipeCreate):
    data = load_data(FILE)
    recipe_id = str(uuid.uuid4())
    new_recipe = Recipe(id=recipe_id, title=recipe.title)
    data[recipe_id] = new_recipe.dict()
    save_data(FILE, data)
    return recipe_id