from typing import Optional
import datetime
from sqlmodel import Field, SQLModel


class QuerType(SQLModel):
    # Aadhaar_key: str
    e: bool = False
    gender: bool = False
    m: bool = False
    name: bool = False
    status: bool = False
    careof: bool = False
    country: bool = False
    dist: bool = False
    house: bool = False
    landmark: bool = False
    loc: bool = False
    pc: bool = False
    po: bool = False
    state: bool = False
    street: bool = False
    subdist: bool = False
    vtc: bool = False



class Aadhaar(SQLModel):
    id: Optional[int] = Field(default=None, primary_key=True)
    dob: str
    aadhaar_key: str
    timestamp: datetime.datetime = Field(default=datetime.datetime.now())
    e: Optional[str] = Field(default=None)
    gender: str
    m: str
    name: str
    status: str
    careof: str
    country: str
    dist: str
    house: str
    landmark: str
    loc: str
    pc: str
    po: str
    state: str
    street: str
    subdist: str
    vtc: str