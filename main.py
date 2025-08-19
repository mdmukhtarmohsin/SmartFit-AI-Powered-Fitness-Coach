from fastapi import FastAPI, Depends
from controllers.user import users_router
from controllers.workouts import workouts_router
from controllers.excercises import excercises_router
from controllers.nutrition import nutritions_router

app = FastAPI()

app.include_router(users_router)
app.include_router(workouts_router)
app.include_router(excercises_router)
app.include_router(nutritions_router)

@app.get("/")
def read_root():
    return {"Hello": "World"}