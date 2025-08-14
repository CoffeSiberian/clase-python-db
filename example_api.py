from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from db import selectDataEjemplo
from db import selectDataPerro as SeleccionarPerro
from db import selectDataDuenos as SeleccionarDuenos

from db import selectExampleData

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
def read_root(request: Request):
    return templates.TemplateResponse(
        request=request, name="index.html", context={"title": "Hola Mundo!!!"}
    )

@app.get("/perros", response_class=HTMLResponse)
def duhsdjkhfbsdkfb(request: Request):
    db_ejemplo = selectDataEjemplo()

    contexto = {
        "ejemplo": db_ejemplo,
        "title": "Lista Perritos 🦊"
    }
    
    return templates.TemplateResponse(
        request=request, name="listaperros.html", context=contexto
    )

@app.get("/perros/agregar")
def otra_pagina_2 (request: Request):
    return templates.TemplateResponse(
        request=request, name="formulario.html"
    )

@app.get("/perros/")
def read_perros():
    return SeleccionarPerro()

@app.get("/duenos/")
def read_duenos():
    return SeleccionarDuenos()

@app.get("/example/")
def read_example():
    res = selectExampleData()
    
    return {
        "respuesta": res
    }