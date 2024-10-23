from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from router import prediction


app = FastAPI()

app.include_router(prediction.router)

app.mount("/static",StaticFiles(directory="static"),name="static")