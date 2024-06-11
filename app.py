from controller.userController import createUser
from config.estructure import create_database


if __name__ == '__main__':
    create_database()
    

# create users
createUser('Ana', 32)
createUser('Miguel', 30)
createUser('Juan', 42)