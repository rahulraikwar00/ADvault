from fastapi import FastAPI
from advault.db import crud, database, models, schemas

app = FastAPI()


@app.get("/")
async def create():
    database.cr_db()
    print("Database created")


@app.pst("/upload")
async def upload(data: models.Poa_Sat):
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
