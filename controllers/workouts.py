from fastapi import APIRouter

workouts_router = APIRouter(prefix='/workouts')

@workouts_router.get("/")
def get_workouts():
    pass

@workouts_router.get("/{workout_id}")
def get_workout_by_id(workout_id:int):
    pass

@workouts_router.post("/")
def create_workout():
    pass

@workouts_router.patch("/{workout_id}")
def update_workout(workout_id:int):
    pass

@workouts_router.delete("/{workout_id}")
def delete_workout(workout_id:int):
    pass