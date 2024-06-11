from config.database import Base, engine
from models.book import Book
from models.users import User

def create_database():
    Base.metadata.create_all(bind=engine)