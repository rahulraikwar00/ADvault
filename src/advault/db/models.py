from typing import Optional
import datetime
from sqlmodel import Field, SQLModel


class Ad_Hub(SQLModel, table=True):
    id: Optional[int] = Field(default=None)
    aadhaar_key: str = Field(primary_key=True)
    uid: str


class Poi_Sat(SQLModel, table=True):
    id: Optional[int] = Field(default=None,primary_key=True)
    aadhaar_key :str = Field(foreign_key="ad_hub.aadhaar_key")
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

class Poa_Sat(SQLModel, table=True):
    id: Optional[int] = Field(default=None,primary_key=True)
    aadhaar_key :str = Field(foreign_key="ad_hub.aadhaar_key")
    dob: str
    e: Optional[str] = Field(default=None)
    gender: str
    m: str
    name: str


class Ad_Aud_Link(SQLModel, table=True):
    ad_aud_key: str = Field(primary_key=True)
    aadhaar_key: str = Field(foreign_key="ad_hub.aadhaar_key")
    audit_key: str = Field(foreign_key="audit_hub.audit_key")


class AD_salt_sat(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    salt: str = Field(primary_key=True)
    aadhaar_key: str = Field(foreign_key="ad_hub.aadhaar_key")


class Audit_Hub(SQLModel, table=True):
    audit_key: str = Field(primary_key=True)
    timestamp: datetime.datetime = Field(default=datetime.datetime.now())


# creater server audit tabl
class Server_Audit_Sat(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    audit_key: str = Field(foreign_key="audit_hub.audit_key")
    timestamp: datetime.datetime = Field(default=datetime.datetime.now())
    status: str = Field(default="pending")
    reason: str = Field(default="")
    action: str = Field(default="")
    action_by: str = Field(default="")
    action_on: datetime.datetime = Field(default=datetime.datetime.now())
    action_remarks: str = Field(default="")


# create user audits table
class User_Audit_Sat(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    audit_key: str = Field(foreign_key="audit_hub.audit_key")
    timestamp: datetime.datetime = Field(default=datetime.datetime.now())
    status: str = Field(default="pending")
    reason: str = Field(default="")
    action: str = Field(default="")
    action_by: str = Field(default="")
    action_on: datetime.datetime = Field(default=datetime.datetime.now())
