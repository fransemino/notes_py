from flask_classy import FlaskView
from flask import jsonify
from schemas import TaskSchema, TaskStatusSchema
from models.task_model import Task
from utils import *
from database import db
from werkzeug.exceptions import BadRequest, InternalServerError




class TasksView(FlaskView):

    task_schema = TaskSchema()
    status_schema = TaskStatusSchema()

    def index(self):
        user = authorization()
        if user == 0:
            raise BadRequest('please login')
        else:
            tasks = Task.query.filter(Task.owner == user.id_user)
            tasks_data = self.task_schema.dump(tasks, many=True).data
            return jsonify(tasks_data)


    def get(self, id_task):
        user = authorization()
        if user == 0:
            raise BadRequest('please login')
        else:
            task = Task.query.filter(user.id_user == Task.owner).filter(Task.id_task == int(id_task)).first()
            task_data = self.task_schema.dump(task).data
            return jsonify({'task': task_data})

    def post(self):
        user = authorization()
        if user == 0:
            raise BadRequest('please login')
        else:
            data = request.json
            task_name = data.get('task_name', None)
            task_status = data.get('task_status')
            due_date = data.get('due_date')
            if not task_name:
                raise BadRequest('Task name is None')
            tsk = Task()
            tsk.task_name=task_name
            tsk.owner = user.id_user
            if task_status == "ready":
                tsk.id_task_status=1
            elif task_status == "doing":
                tsk.id_task_status=2
            elif task_status == "done":
                tsk.id_task_status=3
            if due_date is not None :
                tsk.due_date = due_date
            try:
                db.session.add(tsk)
                db.session.commit()
            except Exception as e:
                db.session.rollback()
                raise InternalServerError('Task not added')
            task_data = self.task_schema.dump(tsk).data
            return jsonify({'task': task_data})

    def put(self, id_task):
        user=authorization()
        if user == 0:
            raise BadRequest('please login')
        else:
            task_from_bd = Task.query.filter(Task.owner == user.id_user).filter(Task.id_task == id_task).first()
            task=Task()
            task.id_task = task_from_bd.id_task
            data = request.json
            task_name = data.get('task_name', None)
            task_status = data.get('task_status')
            due_date = data.get('due_date')
            task.task_name = task_name
            task.due_date = due_date
            if task_status == "ready":
                task.id_task_status=1
            elif task_status == "doing":
                task.id_task_status=2
            elif task_status == "done":
                task.id_task_status=3
            try:
                db.session.merge(task)
                db.session.commit()
            except Exception as e:
                db.session.rollback()
                raise InternalServerError('Task not modified')
            task_data = self.task_schema.dump(task_from_bd).data
            return jsonify({'task': task_data})


    def delete(self, id_task):
        user = authorization()
        task = Task.query.filter(user.id_user == Task.owner).filter(Task.id_task == int(id_task)).first()
        try:
            db.session.delete(task)
            db.session.commit()
        except Exception as e:
            return jsonify({'result': False})
        return jsonify({'result': True})
