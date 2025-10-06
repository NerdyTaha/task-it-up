from backend.app import db, bcrypt
from sqlalchemy.orm import relationship

class User(db.Model):
    __tablename__ = "users"
    
    #columns
    id = db.Column(db.Integer, primary_key = True)
    email = db.Column(db.String(120), unique = True, nullable = False)
    password = db.Column(db.String(70), nullable = False) # setting password length 60 because that is the length of bcrypt hashes
    
    #Relationship
    tasks = relationship('Task', backref='user', lazy='true', cascade='all, delete-orphan')

    def __init__(self, email, password):
        self.email = email
        self.password = bcrypt.generate_password_hash(password).decode('utf-8')

