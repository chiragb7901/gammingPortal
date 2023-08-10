from app.main import db
from datetime import datetime

class User(db.Model):

    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), nullable=False)
    public_id = db.Column(db.String(50), unique = True)
    created_at =  db.Column(db.DateTime, default=datetime.utcnow,nullable=False)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow,nullable=False)
    password = db.Column(db.String(255), nullable=False)
    role = db.Column(db.String(50), nullable=False)
    balance = db.Column(db.Integer, nullable=False)

    def create(self):
       db.session.add(self)
       db.session.commit()
       return self
    
    def update(self):
       db.session.add(self)
       db.session.commit()
       return self
    

    def delete(self):
       db.session.delete(self)
       db.session.commit()
       return self

    def __init__(self, username,public_id, password, role, balance):
        self.username = username
        self.balance = balance
        self.public_id = public_id
        self.role = role
        self.password = password

    def __repr__(self):
        return "<{}:{}>".format(id, self.first_name + " " + self.last_name)
    

@db.event.listens_for(User, 'before_insert')
def set_created_at(mapper, connection, target):
    target.created_at = datetime.utcnow()

@db.event.listens_for(User, 'before_update')
def set_updated_at(mapper, connection, target):
    target.updated_at = datetime.utcnow()