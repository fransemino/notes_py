from flask_classy import FlaskView
from flask import jsonify
from sqlalchemy import Date
from schemas import *
from werkzeug.exceptions import BadRequest, InternalServerError
from utils import *
from models import *
from database import *


class UserView(FlaskView):
    user_schema = UserSchema()


    def get(self):
        user = authorization()
        if user == 0:
            raise BadRequest('login please')
        else:
            user_data = self.user_schema.dump(user).data
            return jsonify({'user': user_data})

    def post(self):
        username = request.json.get('username')
        password = request.json.get('password')
        name = request.json.get('name')
        lastname = request.json.get('lastname')
        birthday = request.json.get('birthday')
        if username is None or password is None or name is None or lastname is None or birthday is None:
            raise BadRequest('Missing Information')
        if User.query.filter(User.username == username).first() is not None:
            raise BadRequest('Username already taken')
        user = User()
        user.username = username
        user.password = password
        user.name = name
        user.lastname = lastname
        user.birthday = birthday
        try:
            db.session.add(user)
            db.session.commit()
        except Exception as e:
            db.session.rollback()
            raise InternalServerError('user not added')
        user_data = self.user_schema.dump(user).data
        return jsonify({'user': user_data})

    def put(self):
        user = authorization()
        if user == 0:
            raise BadRequest('login please')
        else:
            username = request.json.get('username')
            password = request.json.get('password')
            name = request.json.get('name')
            lastname = request.json.get('lastname')
            birthday = request.json.get('birthday')
            user_instance = User()
            user_instance.id_user=user.id_user
            if username is not None :
                user_instance.username = username
            if password is not None:
                user_instance.password=password
            if name is not None:
                user_instance.name = name
            if lastname is not None:
                user_instance.lastname = lastname
            if birthday is not None:
                user_instance.birthday = birthday
            try:
                db.session.merge(user_instance)
                db.session.commit()
            except Exception as e:
                db.session.rollback()
                raise InternalServerError('user not modified')
            user_data = self.user_schema.dump(user).data
            return jsonify({'user': user_data})
        return

    def delete(self):
        user = authorization()
        if user == 0 :
            raise BadRequest('login please')
        try:
            db.session.delete(user)
            db.session.commit()
        except Exception as e:
            raise InternalServerError('user not deleted')
        return jsonify({'result': True})
