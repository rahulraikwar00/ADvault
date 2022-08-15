from re import template
from fastapi import FastAPI, Form, Request
from .database import *
from advault.db.database import *
from sqlmodel import select, insert, update, delete, Session


def get_db():
    db = Session(engine)
    return db


def ins_data_hub(data: Ad_Hub):
    with get_db() as db:
        db.add(data)
        db.commit()
        return data


def ins_data_demo(data: DemoHub):
    with get_db() as db:
        db.add(data)
        db.commit()
        return data


def ins_data_ADm_link(data: AdDm_Link):
    with get_db() as db:
        db.add(data)
        db.commit()
        return data


def ins_data_satellite(data: Ad_Satellite):
    with get_db() as db:
        db.add(data)
        db.commit()
        return data
