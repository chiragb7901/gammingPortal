from app.main import db
from datetime import datetime

class Transaction(db.Model):

    __tablename__ = 'transaction'

    id = db.Column(db.Integer, primary_key=True)
    created_at =  db.Column(db.DateTime, default=datetime.utcnow,nullable=False)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow,nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    game_id = db.Column(db.Integer, db.ForeignKey('game.id'))
    bid_price = db.Column(db.Integer, nullable=False)
    result = db.Column(db.String(20), nullable=False)
    price = db.Column(db.Integer, nullable=False)

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

    def __init__(self,user_id,game_id,bid_price,result,price):
        self.user_id = user_id
        self.game_id = game_id
        self.bid_price = bid_price
        self.result = result
        self.price = price

    def __repr__(self):
        return "<{}:{}>".format(id, self.first_name + " " + self.last_name)
    

@db.event.listens_for(Transaction, 'before_insert')
def set_created_at(mapper, connection, target):
    target.created_at = datetime.utcnow()

@db.event.listens_for(Transaction, 'before_update')
def set_updated_at(mapper, connection, target):
    target.updated_at = datetime.utcnow()