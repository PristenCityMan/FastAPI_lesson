from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()


async def read_root():
    return {"message": "Hello world!"}


@app.get("/")
def home():
    return {"message": "This message!", "content": None}


@app.get("/html/")
def html():
    return """<h1>Hello world From HTML</h1>"""
