from utils.json_store import load_data, save_data
from schemas.users import User

FILE = "data/users.json"

def store_new_user(new_user: User):
    users = load_data(FILE)
    users[new_user.id] = {"user_id": new_user.id, "name": new_user.name, "email": new_user.email, "password": new_user.password}
    save_data(FILE, users)
    return new_user.id

def get_user(user_id: str):
    users = load_data(FILE)
    return users.get(str(user_id), None)

def find_user(email: str):
    users = load_data(FILE)
    for user_id, user in users.items():
        if user["email"] == email:
            return user_id
    return None