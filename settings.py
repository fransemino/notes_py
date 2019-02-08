import os

class DBSettings:
    #add db information
    DB_ENGINE = "mysql+pymysql"
    DB_HOST = os.getenv("RDS_HOSTNAME","ec2-107-20-183-142.compute-1.amazonaws.com")
    DB_NAME = os.getenv("RDS_DB_NAME","d72gp2o1uakrnr")
    DB_PORT = os.getenv("RDS_PORT","5432")
    DB_USER = os.getenv("RDS_USERNAME","ccafpecdlitslf")
    DB_PASSWORD = os.getenv("RDS_PASSWORD","567d704d9fdb9b36e3ca482ad6733ccf5f93092ca5829315d2204633e80422b3")
    SQLALCHEMY_DATABASE_URI = "{0}://{1}:{2}@{3}:{4}/{5}".format(DB_ENGINE, DB_USER, DB_PASSWORD, DB_HOST, DB_PORT, DB_NAME)
