import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


DB_USER = os.getenv('DB_USER')
DB_PASS = os.getenv('DB_PASS')
DB_PORT = os.getenv('DB_PORT')
DB_HOST = os.getenv('DB_HOST')

engine = create_engine('mariadb+mariadbconnector://{}:{}@{}:{}/incubator?charset=utf8'.format(
    'root', '2133', '127.0.0.1', '3306'
    ), echo=True)
engine.connect()

Session = sessionmaker(bind=engine)

session = Session()
