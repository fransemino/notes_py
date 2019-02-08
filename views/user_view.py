from flask_classy import FlaskView
from flask import jsonify
from database import db
from sqlalchemy import DateTime
from schemas import *
from werkzeug.exceptions import BadRequest, InternalServerError
from utils import *
from models import User



class UserView(FlaskView):

    user_schema = TaskSchema()

    def index(self):
        return 0

    def get(self):
        user = authorization()
        if user == 0:
            raise BadRequest('login please')
        else:
            response = User.query.filter(User.id_user == user.id_user).first()
            user_data = self.user_schema.dump(response).data
            return jsonify({'user': user_data})

    def post(self):
        username = request.json.get('username')
        password = request.json.get('password')
        name = request.json.get('name')
        lastname = request.json.get('lastname')
        birthday = request.json.get('birthday')
        if username is None or password is None or name is None or lastname is None or birthday is None:
            raise BadRequest('Missing Information')
        if User.query.filter_by(username = username).first() is not None:
            raise BadRequest('Username already taken')
        user = User()
        user.username = username
        user.password = password
        user.name = name
        user.lastname = lastname
        user.birthday = DateTime(birthday)
        try:
            db.session.add(user)
            db.session.commit()
        except Exception as e:
            db.session.rollback()
            raise InternalServerError('user not added')
        user_data = self.user_schema.dump(user).data
        return jsonify({'user': user_data})

    def post(self):
        return

    def delete(self):
        return
