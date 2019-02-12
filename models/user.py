from sqlalchemy import Integer,Date , String
from database import db



class User(db.Model):
    __tablename__ = 'users'
    id_user = db.Column(Integer, primary_key=True)
    username = db.Column(String(150), nullable=False,unique=True)
    password = db.Column(String(128))
    name = db.Column(String(100),nullable=False)
    lastname = db.Column(String(80), nullable=False)
    birthday = db.Column(Date, nullable=False)


    def __setattr__(self, att, value):
        self.__dict__[att] = value