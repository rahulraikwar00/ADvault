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


class Ad_Hub(SQLModel, table=True):
    aadhaar_key: str = Field(primary_key=True)
    uid: str


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


class Poa_Sat(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    aadhaar_key: str = Field(foreign_key="ad_hub.aadhaar_key")
    timestamp: datetime.datetime = Field(default=datetime.datetime.now())
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


class Poi_Sat(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    aadhaar_key: str = Field(foreign_key="ad_hub.aadhaar_key")
    timestamp: datetime.datetime = Field(default=datetime.datetime.now())
    dob: str
    e: Optional[str] = Field(default=None)
    gender: str
    m: str
    name: str


# autdit_logs
class Ad_Aud_Link(SQLModel, table=True):
    ad_aud_key: Optional[int] = Field(default=None, primary_key=True)
    aadhaar_key: str = Field(foreign_key="ad_hub.aadhaar_key")
    audit_key: str = Field(foreign_key="audit_hub.audit_key")


class AD_salt_sat(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    aadhaar_key: str = Field(foreign_key="ad_hub.aadhaar_key")
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
