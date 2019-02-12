from models import User
from werkzeug.exceptions import NotFound
from flask import request


def authorization():
    auth = request.authorization
    username = auth.username
    password = auth.password
    user = User.query.filter(User.username == username).first()
    if user == None or user.password != password:
        return 0
    else:
        return user