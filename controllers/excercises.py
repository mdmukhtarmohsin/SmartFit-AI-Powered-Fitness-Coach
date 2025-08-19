from sys import prefix
from fastapi import APIRouter, FastAPI
from pydantic import BaseModel

excercises_router = APIRouter(prefix='/excercises')

@excercises_router.get("/")
def get_excercises():
    pass

@excercises_router.get("/{excercise_id}")
def get_excercise_by_id(excercise_id:int):
    pass

@excercises_router.post("/")
def create_excercise():
    pass

@excercises_router.patch("/{excercise_id}")
def update_excercise(excercise_id:int):
    pass

@excercises_router.delete("/{excercise_id}")
def delete_excercise(excercise_id:int):
    pass