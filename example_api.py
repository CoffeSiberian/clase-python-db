from fastapi import FastAPI

from db import selectDataPerritos as SeleccionarPerro
from db import selectDataDuenos as SeleccionarDuenos


app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World 4F"}

@app.get("/perros/")
def read_perros():
    return SeleccionarPerro()

@app.get("/duenos/")
def read_duenos():
    return SeleccionarDuenos()