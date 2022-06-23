import os

DB_USER = os.getenv('DB_USER', '')
DB_PASS = os.getenv('DB_PASS', '')
DB_PORT = os.getenv('DB_PORT', '')
DB_HOST = os.getenv('DB_HOST', '')


class BaseConfiguration():
    DEBUG = True
    SECRET_KEY = os.getenv('SECRET_KEY', '')

    '''SQLALCHEMY_DATABASE_URI = 'mariadb+mariadbconnector://{}:{}@{}:{}/incubator?charset=utf8'.format(
        DB_USER, DB_PASS, DB_HOST, DB_PORT
    )'''



    DEBUG_TB_ENABLED = True
    DEBUG_TB_INTERCEPT_REDIRECTS = False
    SQLALCHEMY_TRACK_MODIFICATIONS = True


class PyConfiguration(BaseConfiguration):
    DEBUG_TB_ENABLED = False
