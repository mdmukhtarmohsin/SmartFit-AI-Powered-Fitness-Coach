from fastapi import FastAPI, Depends

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}