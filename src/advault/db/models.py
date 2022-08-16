from typing import Optional
import datetime
from sqlmodel import Field, SQLModel


class Ad_Hub(SQLModel, table=True):
    id: Optional[int] = Field(default=None)
    adhar_key: str = Field(primary_key=True)
    uid: str


class DemoHub(SQLModel, table=True):
    id: Optional[int] = Field(default=None)
    demo_key: str = Field(primary_key=True)


class AdDm_Link(SQLModel, table=True):
    ad_demo_key: str = Field(primary_key=True)
    adhar_key: str = Field(foreign_key="ad_hub.adhar_key")
    demo_key: str = Field(foreign_key="demohub.demo_key")


class Ad_Satellite(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    adhar_key: str = Field(foreign_key="ad_hub.adhar_key")
    name: str
    dob: datetime.datetime
    gender: str
    phone: str
    email: str
    street: str
    vtc: str
    subdist: str
    district: str
    state: str
    pincode: int


class All_Data(SQLModel):
    hub = Field(Ad_Hub)
    demo = Field(DemoHub)
    adm_link = Field(AdDm_Link)
    satellite = Field(Ad_Satellite)
