from app.extensions import db
import datetime



class Chore(db.Model):
    __tablename__ = "chores"
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100))
    name = db.Column(db.String(100))
    notes = db.Column(db.String(300))
    is_completed = db.Column(db.Boolean())
    date_entered = db.Column(db.Date())
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    user = db.relationship("User", back_populates="chores")



    def __init__(self, item):
        self.name = item["name"][0]
        self.title = message["title"][0]

        self.notes = item["notes"][0]
        self.is_completed = False

        self.date_entered = datetime.datetime.now()


    def __repr__(self):
        item ={
            "id":self.id,
            "title":self.title,
            "name":self.name,
            "notes":self.notes,
            "date_entered":self.date_entered,
            "is_completed":self.is_completed,
            "user_id":self.user_id,
            "user":self.user,
        }

        return item
