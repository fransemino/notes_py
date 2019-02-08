from models import User
from werkzeug.exceptions import NotFound
from flask import request


def authorization():
    auth = request.authorization
    username = auth.username
    password = auth.password
    user = User.query.filter(username==User.username).filter(password==User.password)
    if user == None:
        return 0
    else:
        return user