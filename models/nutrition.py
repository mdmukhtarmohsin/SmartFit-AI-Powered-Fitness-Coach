from pydantic import BaseModel
from datetime import date

class Nutrition(BaseModel):
    id:str
    user_id:str
    date:date
    meals:str
    calories:int
    macros:str