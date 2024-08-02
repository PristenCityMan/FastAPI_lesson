from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.requests import Request

app = FastAPI()

templates = Jinja2Templates(directory="templates")


async def read_root():
    return {"message": "Hello world!"}


@app.get("/")
def home():
    return {"message": "This message!", "content": None}


@app.get("/html/", response_class=HTMLResponse)
def html():
    return """<h1>Hello world From HTML</h1>"""


@app.get("/template/", response_class=HTMLResponse)
def template(request: Request):
    context = {"request": request, "header": "New page", "message": "Simple message"}

    return templates.TemplateResponse("index.html", context)
