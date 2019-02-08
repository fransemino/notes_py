from models import *
from werkzeug.exceptions import NotFound
from flask import request


def authorization():
    auth = request.authorization
    username = auth.username
    password = auth.password
    #add logic
    return user