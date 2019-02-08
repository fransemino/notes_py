from sqlalchemy import Column, Integer, ForeignKey, DateTime, Password #add all primary types that are going to be used
from database import db
from passlib.apps import custom_app_context as pwd_context



class User(db.Model):
    __tablename__ = 'users'
    id_user = db.Column(Integer, primary_key=True)
    username = db.Column(String(150), nullable=False,unique=True)
    password = db.Column(String(128))
    name = db.Column(String(100),nullable=False)
    lastname = db.Column(String(80), nullable=False)
    birthday = db.Column(DateTime,nullable=False)


    def __init__(self):


    def hash_password(self, password):
        self.password_hash = pwd_context.encrypt(password)

    def verify_password(self, password):
        return pwd_context.verify(password, self.password_hash)