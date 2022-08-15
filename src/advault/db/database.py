from sqlmodel import SQLModel, create_engine, Session

from db.models import *


#database url for mysql

SQLALCHEMY_DATABASE_URL = "mysql+pymysql://root:1234@localhost:3306/advault"
# url = "postgresql://postgres:root@localhost:5432/advault"
# if not sqlalchemy_utils.functions.database_exists(url):
#     sqlalchemy_utils.functions.create_database(url)
engine = create_engine(SQLALCHEMY_DATABASE_URL, echo=True)


def cr_db():
    SQLModel.metadata.create_all(engine)
    #  create all the tables in the database
def return_data():
    engine.execute("SELECT * FROM pg_catalog.pg_database WHERE datname =  'advault'")
