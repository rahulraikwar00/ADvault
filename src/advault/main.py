from re import template
from fastapi import FastAPI, Form, Request
from db.models import *
from db.database import *
from sqlmodel import select, insert, update, delete

app = FastAPI()

@app.get("/")
async def create():
    cr_db()
    print("Database created")
    # cr_db()  # database and table created
    