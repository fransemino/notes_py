from sqlalchemy import Column, Integer, ForeignKey #add all primary types that are going to be used
from database import db
import datetime

class Task(db.Model):
    __tablename__ = 'tasks'
    id_task = db.Column(Integer, primary_key=True)
    task_name = db.Column(String(150), nullable=False)
    id_task_status = db.Column(Integer, ForeignKey('task_statuses.id_task_status'))
    description = db.relationship('TaskStatus', backref=db.backref('task status per task'))
    #add needed fields

    def __init__(self, task_name=None, id_task_status=1):
        self.task_name = task_name
        self.id_task_status = id_task_status

class TaskStatus(db.Model):
    __tablename__ = 'task_statuses'
    id_task_status = db.Column(Integer, primary_key=True)
    description = db.Column(String(70))

    def __init__(self, id_task_status=None, description=None):
        self.id_task_status = id_task_status
        self.description = description
