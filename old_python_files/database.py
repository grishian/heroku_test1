import datetime
from sqlalchemy import create_engine, Column, DateTime, Integer
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from config import USER_NAME, PASSWORD, HOST, PORT
from utils import print_title

engine = create_engine('mariadb+mariadbconnector://{}:{}@{}:{}/test_mushroom'.format(USER_NAME, PASSWORD,
                                                                                         HOST, PORT), echo=True)
engine.connect()

Session = sessionmaker(bind=engine)

session = Session()

Base = declarative_base()

class BaseObject(Base):
    __abstract__ = True

    id = Column('PK_ID', Integer, primary_key=True, index=True)
    created_on = Column('F_CREATEON', DateTime, default=datetime.datetime.now())
    updated_on = Column('F_UPDATEDON', DateTime, default=datetime.datetime.now(), onupdate=datetime.datetime.now())

def create_database():
    from mushroom import BaseObject
    from temperature import BaseObject
    from grow_run import BaseObject

    print_title('Adding tables...')
    try:
        Base.metadata.create_all(engine)
    except Exception as e:
        print('Error: {}'.format(e))
    print_title('Tables added.')


def delete_tables():
    from mushroom import Mushroom
    from temperature import Temperature
    from grow_run import GrowRun
    print_title('Deleting tables...')

    Base.metadata.drop_all(engine)

    #Mushroom.__table__.drop(bind=engine)
    #GrowRun.__table__.drop(bind=engine)
    #Temperature.__table__.drop(bind=engine)



    print_title('Tables deleted.')

'''

'''






