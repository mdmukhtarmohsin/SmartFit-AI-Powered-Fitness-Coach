from pydantic import BaseModel

class Excercise(BaseModel):
    id:str
    exercise_name:str
    category:str
    equipment_needed:str
    difficulty:str
    instructions:str
    target_muscles:str
