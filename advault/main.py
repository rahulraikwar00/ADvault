from typing import Union
from fastapi import FastAPI,Depends,HTTPException,status
# import local database file
from db.database import *
from db.crud import *
from db.models import *
from db.schema import *

from fastapi.security import OAuth2PasswordBearer,OAuth2PasswordRequestForm
app = FastAPI()


@app.get("/")
async def create():
    cr_db()
    return {"message": "Database created"}


@app.post("/upload")
async def upload(data: Aadhaar):
    ins_data_hub(data)
    return {"message": "Data uploaded"}


@app.get("/download_all/")
async def download():
    return get_all_data()


@app.post("/download")
async def download(columns: QuerType):
    return get_data_by_columns(columns)

@app.post("/download_by_premsat")
async def download_by_premsat(multiSelctionDropdown: List[select_params] = Query(...)):
    return getDataByParms(multiSelctionDropdown)


#api authentication test

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


fake_users_db = {
    "johndoe": {
        "username": "johndoe",
        "full_name": "John Doe",
        "email": "johndoe@example.com",
        "hashed_password": "fakehashedsecret",
        "disabled": False,
    },
    "alice": {
        "username": "alice",
        "full_name": "Alice Wonderson",
        "email": "alice@example.com",
        "hashed_password": "fakehashedsecret2",
        "disabled": True,
    },
}


def fake_hash_password(password: str):
    return "fakehashed" + password

class User(SQLModel):  #creating a sqlmodel will give user a form to enter username and password
    username: str
    email: Union[str,None]
    full_name: Union[str,None]
    disabled: Union[bool,None]



class UserInDB(User):
    hashed_password: str


def get_user(db, username: str):
    if username in db:
        user_dict = db[username]
        return UserInDB(**user_dict)


def fake_decode_token(token):
    # This doesn't provide any security at all
    # Check the next version
    user = get_user(fake_users_db, token)
    return user


async def get_current_user(token: str = Depends(oauth2_scheme)):
    user = fake_decode_token(token)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid authentication credentials",
            headers={"WWW-Authenticate": "Bearer"},
        )
    return user


async def get_current_active_user(current_user: User = Depends(get_current_user)):
    if current_user.disabled:
        raise HTTPException(status_code=400, detail="Inactive user")
    return current_user


@app.post("/token")
async def login(form_data: OAuth2PasswordRequestForm = Depends()):
    user_dict = fake_users_db.get(form_data.username)
    if not user_dict:
        raise HTTPException(status_code=400, detail="Incorrect username or password")
    user = UserInDB(**user_dict)
    hashed_password = fake_hash_password(form_data.password)
    if not hashed_password == user.hashed_password:
        raise HTTPException(status_code=400, detail="Incorrect username or password")
    return {"access_token": user.username, "token_type": "bearer"}


@app.get("/users/me")
async def read_users_me(current_user: User = Depends(get_current_active_user)):
    return current_user

















# class me:
#     nm=''
#     def __init__(self):
#         self.nm = 'pooja'

@app.get("/items/user")
async def get_current_user(token: str = Depends(oauth2_scheme)):# oauth2_scheme is called and converted to string by depends
    user = fake_decode_token(token)
    return user

# @app.get("/items/me")
# async def read_items_me(token :me= Depends()): #depends without any parameter returns the default request body of type
#     # 'me' that is a user defined class whose values are initialized by the constructor. In case no constructor
#     #is provided empty dict will be returned
#     # current output :
#     # {nm:pooja}
#     return token
# @app.get("/items/user")
# async def read_items_user(token :User= Depends()): #depends without any parameter returns the default request body of type
#     # 'me' that is a user defined class whose values are initialized by the constructor. In case no constructor
#     #is provided empty dict will be returned
#     # current output :
#     # {nm:pooja}
#     return token