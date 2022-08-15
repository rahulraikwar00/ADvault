from re import template
from fastapi import FastAPI, Form, Request
from advault.db.models import *
from advault.db.database import *
from advault.db.crud import *
from sqlmodel import select, insert, update, delete, Session


app = FastAPI()


@app.get("/")
async def create():
    cr_db()
    print("Database created")


@app.post("/insert")
def insert_hub(data: Ad_Hub):
    ins_data_hub(data)
    print("Data inserted")
    return data


@app.post("/insert_demo")
def insert_demo(data: DemoHub):
    ins_data_demo(data)
    print("Data inserted")
    return data


@app.post("/insert_adm_link")
def insert_adm_link(data: AdDm_Link):
    ins_data_ADm_link(data)
    print("Data inserted")
    return data


@app.post("/insert_satellite")
def insert_satellite(data: Ad_Satellite):
    ins_data_satellite(data)
    print("Data inserted")
    return data
