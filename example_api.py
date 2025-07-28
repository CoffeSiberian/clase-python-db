from fastapi import FastAPI

from db import selectData as SeleccionarPerro

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/perros/")
def read_perros():
    return SeleccionarPerro()