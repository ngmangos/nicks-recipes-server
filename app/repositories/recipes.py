from utils.json_store import load_data, save_data

FILE = "recipes.json"

def fetch_recipe(recipe_id: int):
    recipes = load_data(FILE)
    return next((recipe for recipe in recipes if recipe["id"] == recipe_id), None)

def save_recipe(recipe):
    data = load_data(FILE)
    data.append(recipe.dict())
    save_data(FILE, data)
    return recipe