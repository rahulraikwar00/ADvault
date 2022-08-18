from .database import *
from .crud import *
from .models import *
from Engine.user import Democrypt
from sqlmodel import select, insert, update, delete, Session
import hashlib


def get_db():
    db = Session(engine)
    return db


def ins_data_hub(data: Aadhaar):
    with get_db() as db:
        # tdata = Democrypt()
        # ad_key = tdata.encrypt(data.aadhaar_key)
        # uid_no = tdata.encrypt(data.aadhaar_key)+"salt"
        adHub_entry = Ad_Hub(
            aadhaar_key=hashlib.sha256(data.aadhaar_key.encode("utf-8")).hexdigest(),
            uid=hashlib.sha256((data.aadhaar_key+"SALT").encode("utf-8")).hexdigest()
        )
        db.add(adHub_entry)
        poi_entry = Poi_Sat(
            dob=data.dob, e=data.e, name=data.name, gender=data.gender, m=data.m
        )
        db.add(adHub_entry)
        db.add(poi_entry)
        db.commit()
        return {"message": "Data uploaded"}


# imp concept of hashing

# 1234 +salt-> abcd | asdnafksndknfakjsndkfjnaksdnfkajnds12k3n1k

# sha256(1234) -> asdnafksndknfakjsndkfjnaksdnfkajnds12k3n1ksha


# pooja30gb.pdf+ 124566 -> pooja30gb.cypt

# sha256(pooja30gb.pdf )-> asdnafksndknfakjsndkfjnaksdnfkajnds12k3n1ksha
# pooja30gb.pdf -> pooja30gb.cypt
