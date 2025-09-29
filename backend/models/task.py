from backend.models import User 
from backend.app import db

class Task(db.Model):
    
    __tablename__ = "tasks"
    id = db.Column(db.Integer, primary_key = True)
    user_id = db.Column(db.Integer, foreign_key=User.user_id )
    task_name = db.Column(db.String(300))

    def __init__(self, user_id, task_name):
        self.user_id = user_id
        self.task_name = task_name