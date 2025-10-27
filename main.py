# pip install fastapi uvicorn jinja2 python-multipart
from fastapi import FastAPI, requests, Form
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

app = FastAPI(title="Lista de alunos")

# Definir a pasta onde está os html
templaytes = Jinja2Templates(directory="templates")

# Definir a pasta onde está os arquivos estáticos (css, imagens e js)
app.mount("/static", StaticFiles(directory="static"), name="static")