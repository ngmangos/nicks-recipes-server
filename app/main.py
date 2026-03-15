from fastapi import FastAPI
from routes import recipes, users, auth
from fastapi.middleware.cors import CORSMiddleware

allow_origins = [
    "http://localhost:8081",  # Expo web
    "http://127.0.0.1:8081",  # Expo web alternative
]

app = FastAPI(
    docs_url="/", # Swagger UI at root
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=allow_origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(recipes.router, prefix="/recipes")
app.include_router(users.router, prefix="/users")
app.include_router(auth.router, prefix="/auth")
