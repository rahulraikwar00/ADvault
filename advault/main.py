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
async def upload(data: Aadhaar):
    ins_data_hub(data)
    return {"message": "Data uploaded"}


@app.get("/download_all/")
async def download():
    return get_all_data()


@app.post("/download")
async def download(columns: QuerType):
    return get_data_by_columns(columns)
