from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from db import selectDataPerritos as SeleccionarPerro
from db import selectDataDuenos as SeleccionarDuenos

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
def read_root(request: Request):
    return templates.TemplateResponse(
        request=request, name="index.html", context={"title": "Hola 4F"}
    )

@app.get("/listaperros", response_class=HTMLResponse)
def read_root(request: Request):
    db_perritos = SeleccionarPerro()
    return templates.TemplateResponse(
        request=request, name="listaperros.html", context={"perritos": db_perritos}
    )

@app.get("/perros/")
def read_perros():
    return SeleccionarPerro()

@app.get("/duenos/")
def read_duenos():
    return SeleccionarDuenos()