import os
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker
from dotenv import load_dotenv

# environment vars
load_dotenv()

ENV = os.environ.get("ENV")
DATABASE = os.environ.get("DATABASE")
HOST = os.environ.get("HOST")
PORT = os.environ.get("PORT")
USERNAME = os.environ.get("USERNAME")
PASSWORD = os.environ.get("PASSWORD") 

# Mysql
mysql_engine = f'mysql://{USERNAME}:{PASSWORD}@{HOST}:{PORT}/{DATABASE}'

# SQlite
sqlite_engine = f'sqlite:///database.sqlite3'

database_engine = sqlite_engine

# check environment
if ENV == 'production':
    database_engine = mysql_engine

# Create database
engine = create_engine(database_engine)
Base = declarative_base()

def session():
    '''It's used to make querys'''
    return sessionmaker(bind=engine)()


def createModels():
    Base.metadata.create_all(bind=engine)