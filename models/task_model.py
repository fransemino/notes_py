from sqlalchemy import Column, Integer, ForeignKey, String,DateTime  #add all primary types that are going to be used
from database import db
import datetime

class Task(db.Model):
    __tablename__ = 'tasks'
    id_task = db.Column(Integer, primary_key=True)
    task_name = db.Column(String(150), nullable=False)
    id_task_status = db.Column(Integer, ForeignKey('task_statuses.id_task_status'))
    description = db.relationship('TaskStatus', backref=db.backref('task status per task'))
    created_date = Column(DateTime, default=datetime.datetime.utcnow)
    owner = db.Column(Integer,ForeignKey('users.id_user'))
    due_date = db.Column(DateTime)

    def __init__(self, task_name=None, id_task_status=1,id_user=0):
        self.task_name = task_name
        self.id_task_status = id_task_status
        self.owner = id_user

    def __setattr__(self, att, value):
        self.__dict__[att] = value

class TaskStatus(db.Model):
    __tablename__ = 'task_statuses'
    id_task_status = db.Column(Integer, primary_key=True)
    description = db.Column(String(70))

    def __init__(self, id_task_status=None, description=None):
        self.id_task_status = id_task_status
        self.description = description
