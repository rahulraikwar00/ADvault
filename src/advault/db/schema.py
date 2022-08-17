from ast import Num
# from pydantic import BaseModel
from sqlmodel import SQLModel

class Aadhaar(SQLModel):
    aadhaar_number: str
    name: str
    dob: str
    gender: str
    phone: int
    email: str
    street: str
    vtc: str
    subdist: str
    district: str
    state: str
    pincode: int
