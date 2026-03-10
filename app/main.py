from fastapi import FastAPI
from routes import recipes, users, auth

app = FastAPI(
    docs_url="/", # Swagger UI at root
)

app.include_router(recipes.router, prefix="/recipes")
app.include_router(users.router, prefix="/users")
app.include_router(auth.router, prefix="/auth")
