from sqlmodel import Session
from fastapi import Query
from typing import List
from enum import Enum
from db.database import engine

class select_params(str, Enum):
    # all queryType parameters
    e = "e"
    gender ="gender"
    m = "m"
    name = "name"
    status = "status"
    careof = "careof"
    country = "country"
    dist = "dist"
    house = "house"
    landmark = "landmark"
    loc = "loc"
    pc = "pc"
    po = "po"
    state = "state"
    street = "street"
    subdist = "subdist"
    vtc = "vtc"

# experimental function -> dropdown selection option for columns

def getDataByParms(multiSelctionDropdown: List[select_params] = Query(...)):
    collstr = [item.value for item in multiSelctionDropdown]
    collstr = ",".join(collstr)
    if len(collstr) < 1:
        collstr = ""
    else:
        collstr = "," + collstr
    with Session(engine) as db:
        data = db.execute(
            f"SELECT ad_hub.aadhaar_key {collstr} FROM ad_hub,poi_sat,poa_sat WHERE ad_hub.aadhaar_key = poi_sat.aadhaar_key and ad_hub.aadhaar_key = poa_sat.aadhaar_key;"
        ).fetchall()
        return data