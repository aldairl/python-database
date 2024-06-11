from sqlalchemy import Column, Integer, String
from config.database import Base

class Book(Base):
    __tablename__ = 'books'
    
    id = Column(Integer, primary_key=True)
    name = Column(String(255), unique=True)
