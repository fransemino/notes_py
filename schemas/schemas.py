from marshmallow import Schema, fields

class TaskStatusSchema(Schema):
    id_task_status = fields.Integer()
    description = fields.String()


class TaskSchema(Schema):
    id_task = fields.Integer()
    task_name = fields.String()
    id_task_status = fields.Integer()
    task_status = fields.Nested(TaskStatusSchema())
    #add needed fields