from fastapi import FastAPI

# import local database file
from db.database import *
from db.crud import *
from db.models import *
app = FastAPI()


@app.get("/")
async def create():
    cr_db()
    return {"message": "Database created"}

@app.post("/upload")
async def upload(data: Aadhaar):
    ins_data_hub(data)
    return {"message": "Data uploaded"}


@app.get("/download/{refrence_id}")
async def download(refrence_id: str):
    pass


@app.get("/download/{refrence_id}/{file_name}")
async def download(refrence_id: str, file_name: str):
    pass