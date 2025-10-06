from backend.app import db

class Task(db.Model):

    __tablename__ = "tasks"

    #columns 
    id = db.Column(db.Integer, primary_key=True)
    task_name = db.Column(db.String(300), nullable=False)
    completed = db.Column(db.Boolean, default=False, nullable=False)
    user_id = db.Column(db.Integer, db.Foreignkey('users.id'), nullable=False)

    def __init__(self, user_id, task_name):
        self.task_name = task_name
        self.user_id = user_id