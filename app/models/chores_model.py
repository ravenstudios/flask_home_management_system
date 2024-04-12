from app.extensions import db
from datetime import datetime



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

    repeat = db.Column(db.Boolean())
    repeat_time = db.Column(db.Integer)

    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    user = db.relationship("User", back_populates="chores", foreign_keys=[user_id])

# <<<<<<< HEAD
    def __init__(self, item):
        self.name = item["name"][0]
        self.title = message["title"][0]

        self.notes = item["notes"][0]
        self.is_completed = False
# =======
    from_user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    from_user = db.relationship("User", back_populates="chores_created", foreign_keys=[from_user_id])

    def __init__(self, chore):
        self.name = chore["name"][0]
        self.notes = chore["notes"][0]
        self.completed = False
# >>>>>>> origin

        self.repeat_time = chore["repeat_time"][0]
        self.date_entered = datetime.now()


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
