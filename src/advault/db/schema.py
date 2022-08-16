from ast import Num
from pydantic import BaseModel

class Aadhaar(BaseModel):
    aadhaar_number: str
    name: str
    dob: str
    gender: str
    phone: int
    email: str
    street: str
    vtc: str
    subdist: str
    district: str
    state: str
    pincode: int



# c- red
# d- green
# e- yellow

# mix - balls