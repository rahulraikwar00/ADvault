from typing import Optional,Union
import datetime
from sqlmodel import Field, SQLModel

class Ad_Hub(SQLModel, table=True):
    aadhaar_key: str = Field(primary_key=True)
    uid: str



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


#user table for api authentication
class User_data(SQLModel,table=True):
    username : str= Field(primary_key=True)
    # password : str
    hashed_password: str 
    disabled: bool



class Token(SQLModel):
    access_token: str
    token_type: str


class TokenData(SQLModel):
    username: Union[str, None] = None


class User(SQLModel):
    username: str
    email: Union[str, None] = None
    full_name: Union[str, None] = None
    disabled: Union[bool, None] = None