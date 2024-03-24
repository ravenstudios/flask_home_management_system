from app.extensions import db
from sqlalchemy.orm import relationship
import datetime



class Message(db.Model):
    __tablename__ = "messages"
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100))
    content = db.Column(db.String(300))
    status = db.Column(db.String(30))

    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    user = db.relationship("User", back_populates="messages")

    date_entered = db.Column(db.Date())
    date_read = db.Column(db.Date())




    def __init__(self, message):
        self.title = message["title"][0]
        self.content = message["content"][0]
        self.status = message["status"][0]
        self.date_entered = datetime.datetime.now()
        self.date_read = None


    def __repr__(self):
        message ={
            "id":self.id,
            # "item_priority":self.item_priority,
            "title":self.title,
            "content":self.content,
            "status":self.item_completed,
            "directed_to":self.directed_to,
            "date_entered":self.date_entered,
            "date_read":self.date_read,
            "user_id":self.user_id,
            "user":self.user,
        }

        return message
