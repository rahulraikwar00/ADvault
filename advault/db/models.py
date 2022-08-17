from typing import Optional
import datetime
from sqlmodel import Field, SQLModel


class Aadhaar(SQLModel):
    aadhaar_key: str = Field(foreign_key="ad_hub.aadhaar_key")
    status: str
    timestamp: datetime.datetime


class Ad_Hub(SQLModel, table=True):
    id: Optional[int] = Field(default=None)
    aadhaar_key: str = Field(primary_key=True)
    uid: str


class Poi_Sat(Aadhaar, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
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


class Poa_Sat(Aadhaar, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    dob: str
    e: Optional[str] = Field(default=None)
    gender: str
    m: str
    name: str


class Ad_Aud_Link(Aadhaar, table=True):
    ad_aud_key: str = Field(primary_key=True)
    audit_key: str = Field(foreign_key="audit_hub.audit_key")


class AD_salt_sat(Aadhaar, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    salt: str = Field(primary_key=True)


class Audit_Hub(SQLModel, table=True):
    audit_key: str = Field(primary_key=True)
    timestamp: datetime.datetime = Field(default=datetime.datetime.now())


# for monitoring purpose
class Audit_Log(SQLModel):
    timestamp: datetime.datetime = Field(default=datetime.datetime.now())
    audit_key: str = Field(foreign_key="audit_hub.audit_key")
    status: str = Field(default="pending")
    reason: str = Field(default="")
    action: str = Field(default="")
    action_by: str = Field(default="")
    action_on: datetime.datetime = Field(default=datetime.datetime.now())
    action_remarks: str = Field(default="")


# creater server audit tabl
class Server_Audit_Sat(Audit_Log, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)


# create user audits table
class User_Audit_Sat(Audit_Log, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
