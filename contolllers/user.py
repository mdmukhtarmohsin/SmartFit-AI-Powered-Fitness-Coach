from sys import prefix
from fastapi import APIRouter, FastAPI

users_router = APIRouter(prefix='/auth')

@users_router.post("/register")
def register_user():
    pass
