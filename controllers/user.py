from fastapi import APIRouter
from pydantic import BaseModel

users_router = APIRouter(prefix='/auth')

class Cred(BaseModel):
    email:str
    password:str

@users_router.post("/register")
def register_user():
    pass

@users_router.post("/login")
def login(cred:Cred):
    pass

@users_router.get("/user/{user_id}")
def get_user(user_id:int):
    pass