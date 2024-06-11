from sqlalchemy.orm import sessionmaker
from models.users import User
from config.database import session

user_session = session()

def createUser(name, age):
    user = User(name=name, age=age)
    user_session.add(user)
    user_session.commit()
    print("user have been added")