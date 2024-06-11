from sqlalchemy import Column, Integer, String
from config.database import Base

class User(Base):
    __tablename__ = 'users'
    
    id = Column(Integer, primary_key=True)
    name = Column(String(255), unique=True)
    age = Column(String(255))
