from app.main import db
from datetime import datetime

class Game(db.Model):

    __tablename__ = 'game'

    id = db.Column(db.Integer, primary_key=True)
    game = db.Column(db.String(20))
    created_at =  db.Column(db.DateTime, default=datetime.utcnow,nullable=False)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow,nullable=False)

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

    def __init__(self, game):
        self.game = game

    def __repr__(self):
        return "<{}:{}>".format(id, self.first_name + " " + self.last_name)
    

@db.event.listens_for(Game, 'before_insert')
def set_created_at(mapper, connection, target):
    target.created_at = datetime.utcnow()

@db.event.listens_for(Game, 'before_update')
def set_updated_at(mapper, connection, target):
    target.updated_at = datetime.utcnow()