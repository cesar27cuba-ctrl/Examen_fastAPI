from fastapi import FastAPI
from sqlmodel import SQLModel

app = FastAPI()


@app.get("/root")
def read_root():
    return {"Hello": "World", " name": "Cesar", "age": 28, "casado": False}
