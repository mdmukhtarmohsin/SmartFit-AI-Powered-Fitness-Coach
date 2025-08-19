from fastapi import FastAPI, Depends
from contolllers.user import users_router
from contolllers.workouts import workouts_router

app = FastAPI()

app.include_router(users_router)
app.include_router(workouts_router)

@app.get("/")
def read_root():
    return {"Hello": "World"}