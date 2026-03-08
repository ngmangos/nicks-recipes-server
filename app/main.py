from fastapi import FastAPI
from routes import recipes

app = FastAPI(
    docs_url="/", # Swagger UI at root
)

app.include_router(recipes.router, prefix="/users")
app.include_router(recipes.router, prefix="/recipes")
