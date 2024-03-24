from app.extensions import db
import datetime



class Chore(db.Model):
    __tablename__ = "chores"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    notes = db.Column(db.String(300))
    completed = db.Column(db.Boolean())
    date_entered = db.Column(db.Date())



    def __init__(self, item):
        self.name = item["name"][0]
        self.notes = item["notes"][0]
        self.completed = False

        self.date_entered = datetime.datetime.now()


    def __repr__(self):
        item ={
            "id":self.id,
            "name":self.name,
            "notes":self.notes,
            "date_entered":self.date_entered,
            "completed":self.completed,
        }

        return item
