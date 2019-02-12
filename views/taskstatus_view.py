from flask_classy import FlaskView
from flask import jsonify
from schemas import TaskStatusSchema
from models.task_model import TaskStatus
from utils import *
from database import db
from werkzeug.exceptions import BadRequest, InternalServerError




class TaskStatusView(FlaskView):

    status_schema = TaskStatusSchema()

    def post(self):
        user = authorization()
        if user == 0:
            raise BadRequest('please login')
        else:
            data = request.json
            description = data.get('description')
            if not description:
                raise BadRequest('description is None')
            tsk_status = TaskStatus()
            tsk_status.description = description
            try:
                db.session.add(tsk_status)
                db.session.commit()
            except Exception as e:
                db.session.rollback()
                raise InternalServerError('Task status not added')
            task_data = self.status_schema.dump(tsk_status).data
            return jsonify({'task status': task_data})
