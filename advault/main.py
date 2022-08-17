from fastapi import FastAPI

# import local database file
from db.database import *
from db.crud import *
from db.models import *
from db.schema import *

app = FastAPI()


@app.get("/")
async def create():
    cr_db()
    return {"message": "Database created"}

@app.post("/upload")
async def upload(data: Poa_Sat):
    pass


@app.get("/download/{refrence_id}")
async def download(refrence_id: str):
    pass


@app.get("/download/{refrence_id}/{file_name}")
async def download(refrence_id: str, file_name: str):
    pass


# request to check if the refrecne id is present in the database
@app.get("/check/{refrence_id}")
async def check(refrence_id: str):
    pass


# @app.post("/aadhar_data_insert")
# def aadhar_data_insert(data: Aadhaar):
#     return data
