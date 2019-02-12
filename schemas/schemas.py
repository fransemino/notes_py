from marshmallow import Schema, fields
from marshmallow_sqlalchemy import ModelSchema
from models import task_model


class TaskStatusSchema(Schema):
    id_task_status = fields.Integer()
    description = fields.String()


class TaskSchema(Schema):
     id_task = fields.Integer()
     task_name = fields.String()
     description = fields.Nested(TaskStatusSchema())


class UserSchema(Schema):

    name = fields.String()
    lastname = fields.String()
    username = fields.String()
    birthday = fields.Date()