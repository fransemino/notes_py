import os

class DBSettings:
    #add db information
    DB_ENGINE = "mysql+pymysql"
    DB_HOST = os.getenv("RDS_HOSTNAME","")
    DB_NAME = os.getenv("RDS_DB_NAME","")
    DB_PORT = os.getenv("RDS_PORT","")
    DB_USER = os.getenv("RDS_USERNAME","")
    DB_PASSWORD = os.getenv("RDS_PASSWORD","")
    SQLALCHEMY_DATABASE_URI = "{0}://{1}:{2}@{3}:{4}/{5}".format(DB_ENGINE, DB_USER, DB_PASSWORD, DB_HOST, DB_PORT, DB_NAME)
