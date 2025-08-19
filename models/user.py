from pydantic import BaseModel

class User(BaseModel):
    id:str
    username:str
    email:str
    password:str
    age:int
    weight:int
    height:int
    goals:str