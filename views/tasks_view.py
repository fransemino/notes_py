from flask_classy import FlaskView
from flask import jsonify
from schemas import *
from utils import *
#from sqlalchemy import or_
from datetime import datetime
from werkzeug.exceptions import BadRequest


class TasksView(FlaskView):
    task_schema = TaskSchema()
    status_schema = TaskStatusSchema()

    def index(self):
        #authorization()
        tasks = Task.query.all()
        tasks_data = self.task_schema.dump(tasks).data
        return jsonify(tasks_data)

    def get(self, id_task):
        #authorization()
        task = Task.query.filter(Task.id_task==int(id_task)).first()
        task_data = self.task_schema.dump(task).data
        return jsonify({'task': task_data})

    def post(self):
        #add fields, queries, try/catch, etc
        user = authorization()
        data = request.json
        task_name = data.get('task_name', None)
        if not task_name:
            raise BadRequest('Task name is None')
        tsk = Task(task_name=task_name)
        try:
            db.session.add(tsk)
            db.session.commit()
        except Exception as e:
            db.session.rollback()
            raise InternalServerError('Task not added')
        task_data = self.task_schema.dump(tsk).data
        return jsonify({'task': task_data})

    def put(self, id_task):
        return


    def delete(self, id_task):
        return
