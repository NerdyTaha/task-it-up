from backend.models import User 
from backend.app import db

class Task(db.Model):

    __tablename__ = "tasks"
    user_id = db.Column()
    task_set = db.Column()