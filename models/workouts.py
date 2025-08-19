from pydantic import BaseModel

class Workouts(BaseModel):
    id:str
    plan_name:str
    difficulty_level:str
    duration:int
    target_muscle_groups:str
    exercises_list:str
