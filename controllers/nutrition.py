from fastapi import APIRouter

nutritions_router = APIRouter(prefix='/nutritions')

@nutritions_router.get("/")
def get_nutritions():
    pass

@nutritions_router.get("/{nutrition_id}")
def get_nutrition_by_id(nutrition_id:int):
    pass

@nutritions_router.post("/")
def create_nutrition():
    pass

@nutritions_router.patch("/{nutrition_id}")
def update_nutrition(nutrition_id:int):
    pass

@nutritions_router.delete("/{nutrition_id}")
def delete_nutrition(nutrition_id:int):
    pass