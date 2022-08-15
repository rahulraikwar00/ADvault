from re import template
from fastapi import FastAPI,Form,Request
from db.models import *
from advault.db.database import *
from sqlmodel import select
from fastapi.templating import Jinja2Templates
app = FastAPI()

@app.get("/")
async def create():
    cr_db() #database and table created