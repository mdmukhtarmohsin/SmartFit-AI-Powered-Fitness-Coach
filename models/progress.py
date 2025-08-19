from pydantic import BaseModel
from datetime import date

class Progress(BaseModel):
    user_id:str
    workout_id:str
    date:date
    exercises_completed:str
    sets: int
    reps:int
    weights:str
    duration:int
    calories_burned:str
    