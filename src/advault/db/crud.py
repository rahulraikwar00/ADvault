from re import template
from fastapi import FastAPI, Form, Request
from .database import *
from advault.db.database import *
from sqlmodel import select, insert, update, delete, Session
from advault.db.schema import *
from .models import *


def get_db():
    db = Session(engine)
    return db


def ins_data_hub(data: Aadhaar):
    with get_db() as db:
        ad_key = data.aadhaar_number
        uid_no = data.aadhaar_number
        adHub_entry = Ad_Hub(aadhaar_key=ad_key,uid = uid_no)
        db.add(adHub_entry)
        # db.add(data)
        db.commit()
        return adHub_entry


# def ins_data_demo(data: DemoHub):
#     with get_db() as db:
#         db.add(data)
#         db.commit()
#         return data


# def ins_data_ADm_link(data: AdDm_Link):
#     with get_db() as db:
#         db.add(data)
#         db.commit()
#         return data


# def ins_data_satellite(data: Ad_Satellite):
#     with get_db() as db:
#         db.add(data)
#         db.commit()
#         return data

# def select_all_data():
#     with get_db() as db:
#         return db.query(Ad_Hub).all()
