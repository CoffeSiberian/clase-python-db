from fastapi import FastAPI, Request, Form, status
from fastapi.params import Form
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from db import insertPerro, selectDataPerritos, deletePerro
from db import selectDataDuenos as SeleccionarDuenos

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
def read_root(request: Request):
    return templates.TemplateResponse(
        request=request, name="index.html", context={"title": "Hola Mundo!!!"}
    )

@app.get("/perros", response_class=HTMLResponse)
def listaPerros(request: Request):
    db_perros = selectDataPerritos()

    contexto = {
        "perros": db_perros,
        "title": "Lista Perritos 🦊"
    }
    
    return templates.TemplateResponse(
        request=request, name="listaperros.html", context=contexto
    )

@app.get("/perros/agregar")
def agregarPerro (request: Request):
    return templates.TemplateResponse(
        request=request, name="formulario.html"
    )

@app.post("/perros/agregar")
def crearPerro(
    request: Request,
    nombre: str = Form(...),
    raza: str = Form(...),
    edad: str = Form(...)
):
    ok = insertPerro(nombre, raza, edad, "e9c33ec7")
    if not ok:
        return templates.TemplateResponse(
            "formulario.html",
            {"request": request, "error": "No se pudo crear el perro."},
            status_code=400,
        )
    return RedirectResponse(url="/perros", status_code=status.HTTP_303_SEE_OTHER)

@app.post("/perros/{perro_id}/eliminar")
def eliminarPerro(perro_id: str):
    ok = deletePerro(perro_id)
    return RedirectResponse(url="/perros", status_code=status.HTTP_303_SEE_OTHER)

@app.get("/duenos/")
def read_duenos():
    return SeleccionarDuenos()