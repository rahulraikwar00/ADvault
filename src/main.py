from fastapi import FastAPI
from advault.db.models import *
from advault.db.database import *
from advault.db.crud import *
# from advault.db.schema import *


app = FastAPI()


@app.get("/")
async def create():
    cr_db()
    print("Database created")


@app.post("/insert")
def insert_hub(data: Aadhaar):
    ins_data_hub(data)
    print("Data inserted")
    return data


# @app.post("/insert_adm_link")
# def insert_adm_link(data: AdDm_Link):
#     ins_data_ADm_link(data)
#     print("Data inserted")
#     return data


# @app.post("/insert_satellite")
# def insert_satellite(data: Ad_Satellite):
#     ins_data_satellite(data)
#     print("Data inserted")
#     return data


# @app.get("/select")
# def select_all():
#     return select_all_data()


# @app.post("/aadhar_data_insert")
# def aadhar_data_insert(data: Aadhaar):
#     return data
