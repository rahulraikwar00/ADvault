from sqlmodel import SQLModel,create_engine,Session
import sqlalchemy_utils 
from db.models import *

url = 'postgresql://postgres:root@localhost:5432/advault'
if not sqlalchemy_utils.functions.database_exists(url):
    sqlalchemy_utils.functions.create_database(url)
engine = create_engine(url,echo=True)

def cr_db():
    SQLModel.metadata.create_all(engine) #create all the tables in the database

