from sqlmodel import SQLModel, create_engine
import sqlalchemy_utils as sa_utils

SQLALCHEMY_DATABASE_URL = "mysql+pymysql://root:1234@localhost:3306/advault2"
# url = "postgresql://postgres:root@localhost:5432/advault"
if not sa_utils.functions.database_exists(SQLALCHEMY_DATABASE_URL):
    sa_utils.functions.create_database(SQLALCHEMY_DATABASE_URL)
engine = create_engine(SQLALCHEMY_DATABASE_URL, echo=True)


def cr_db():
    SQLModel.metadata.create_all(engine)


def drop_db():
    SQLModel.metadata.drop_all(engine)
