from flask_classy import FlaskView
from flask import jsonify
from database import db
from schemas import *
from werkzeug.exceptions import BadRequest, InternalServerError
from utils import *
from models import User
#from sqlalchemy import or_
from flask_httpauth import HTTPBasicAuth


auth = HTTPBasicAuth()

class UserView(FlaskView):

    @app.route('/user/new', methods = ['POST'])
    def new_user(self):
        username = request.json.get('username')
        password = request.json.get('password')
        name = request.json.get('name')
        lastname = request.json.get('lastname')
        birthday = request.json.get('birthday')
        if username is None or password is None or name is None or lastname is None or birthday is None:
            raise InternalServerError('Missing Information')
        if User.query.filter_by(username = username).first() is not None:
            raise InternalServerError('Username already taken')
        user = User(username = username)
        user.hash_password(password)
        db.session.add(user)
        db.session.commit()
        return jsonify({ 'username': user.username }), 201, \
               {'Location': url_for('get_user', id = user.id, _external = True)}

