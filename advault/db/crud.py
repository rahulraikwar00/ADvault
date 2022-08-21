
from .database import *
from .crud import *
from .models import *
from .schema import *
from sqlmodel import Session, select
import hashlib
from features.dropdown import *




def get_db():
    db = Session(engine)
    return db



def inset_ad_hub(data: Aadhaar, aadhaar_key: str, uid: str):
    adHub_entry = Ad_Hub(aadhaar_key=aadhaar_key, uid=uid)
    return adHub_entry


def insert_poi_sat(data: Aadhaar, aadhaar_key: str):
    poi_entry = Poi_Sat(
        aadhaar_key=aadhaar_key,
        dob=data.dob,
        e=data.e,
        name=data.name,
        gender=data.gender,
        m=data.m,
    )
    return poi_entry


def insert_poa_sat(data: Aadhaar, aadhaar_key: str):
    poa_entry = Poa_Sat(
        aadhaar_key=aadhaar_key,
        careof=data.careof,
        country=data.country,
        dist=data.dist,
        house=data.house,
        landmark=data.landmark,
        loc=data.loc,
        pc=data.pc,
        po=data.po,
        state=data.state,
        street=data.street,
        subdist=data.subdist,
        vtc=data.vtc,
        status=data.status,
    )
    return poa_entry

#pass audit_hub sqlmodel as parameter
def inset_audit_hub(audit_key: str):
    audit_entry = Audit_Hub(
        audit_key=audit_key,
        timestamp=datetime.datetime.now(),
    )
    return audit_entry

#pass user_audit_sat sqlmodel as parameter
def insert_user_audit_sat(audit_key: str):
    user_entry = User_Audit_Sat(
        audit_key=audit_key,
        timestamp=datetime.datetime.now(),
        status="status",
        action="action",
        action_by="action_by",
        action_on="action_on",
        action_remarks="action_remarks",
        reason="reason",
    )
    return user_entry

#pass server_audit_sat sqlmodel as parameter
def insert_server_audit_sat(audit_key: str):
    server_entry = Server_Audit_Sat(
        audit_key=audit_key,
        timestamp=datetime.datetime.now(),
        status="status",
        action="action",
        action_by="action_by",
        action_on="action_on",
        action_remarks="action_remarks",
        reason="reason",
    )
    return server_entry


# pass ahadhaar_key and audit_key to this function
def insert_ad_audit_link(aadhaar_key: str, audit_key: str):
    link_entry = Ad_Aud_Link(
        audit_key=audit_key,
        aadhaar_key=aadhaar_key,
    )
    return link_entry


def get_data(reference_id: str):
    with get_db() as db:
        data = db.query(Ad_Hub).filter(Ad_Hub.aadhaar_key == reference_id).first()
        return data


def get_all_data():
    with get_db() as db:
        data = db.execute(
            "SELECT * FROM ad_hub,poi_sat,poa_sat WHERE ad_hub.aadhaar_key = poi_sat.aadhaar_key and ad_hub.aadhaar_key = poa_sat.aadhaar_key;"
        ).fetchall()
        return data


def get_data_by_columns(columns: QuerType):
    collstr = []
    print(collstr)
    for col in columns:
        if col[1]:
            collstr.append(col[0])
    collstr = ",".join(collstr)
    if len(collstr) < 1:
        collstr = ""
    else:
        collstr = "," + collstr
    with get_db() as db:
        data = db.execute(
            f"SELECT ad_hub.aadhaar_key {collstr} FROM ad_hub,poi_sat,poa_sat WHERE ad_hub.aadhaar_key = poi_sat.aadhaar_key and ad_hub.aadhaar_key = poa_sat.aadhaar_key;"
        ).fetchall()
        return data

def ins_data_hub(data: Aadhaar):
    with get_db() as db:
        # for testing purpose
        # aadhaar_key = data.aadhaar_key
        # audit_key = data.aadhaar_key
        # uid = data.aadhaar_key

        aadhaar_key = hashlib.sha256(data.aadhaar_key.encode("utf-8")).hexdigest()
        uid = hashlib.sha256((data.aadhaar_key + "SALT").encode("utf-8")).hexdigest()
        audit_key = hashlib.sha256(
            (
                data.aadhaar_key
                + datetime.datetime.now().strftime("%m/%d/%Y, %H:%M:%S")
            ).encode("utf-8")
        ).hexdigest()

        ad_hub = inset_ad_hub(data, aadhaar_key, uid)
        ad_poa = insert_poa_sat(data, aadhaar_key)
        ad_poi = insert_poi_sat(data, aadhaar_key)

        ad_audit = inset_audit_hub(audit_key)
        ad_user_audit = insert_user_audit_sat(audit_key)
        ad_server_audit = insert_server_audit_sat(audit_key)

        ad_audit_link = insert_ad_audit_link(aadhaar_key, audit_key)
        
        db.add(ad_hub)
        db.add(ad_poa)
        db.add(ad_poi)

        db.add(ad_audit)
        db.add(ad_user_audit)
        db.add(ad_server_audit)
        db.commit()

        db = Session(engine)
        db.add(ad_audit_link)
        db.commit()
        
        return {"message": "Data uploaded"}

#get user data for authentication
def get_all_users()->dict:
    with get_db() as db:
        res = db.exec(
            "SELECT * FROM user_data;"
        ).fetchall()
        return res

from passlib.context import CryptContext
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def register_users():
    with get_db() as db:
        user1 = User_data(username='pooja',hashed_password = pwd_context.hash('12345'),disabled = False)
        user2 = User_data(username='rahul',hashed_password = pwd_context.hash('67890'),disabled = False)
        user3 = User_data(username='aarti',hashed_password = pwd_context.hash('67582'),disabled = False)
        db.add(user1)
        db.add(user2)
        db.add(user3)
        db.commit()
        
