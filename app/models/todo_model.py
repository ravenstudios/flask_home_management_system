from app.extensions import db
import datetime



class Item(db.Model):
    __tablename__ = "todo_list"
    id = db.Column(db.Integer, primary_key=True)
    priority = db.Column(db.Integer)
    name = db.Column(db.String(100))
    notes = db.Column(db.String(300))
    completed = db.Column(db.Boolean())
    date_entered = db.Column(db.Date())
    date_completed = db.Column(db.Date())

    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    user = db.relationship("User", back_populates="todo_list")


    def __init__(self, item):
         # Auto-increment item_priority based on existing priorities
        max_priority = db.session.query(db.func.max(Item.priority)).scalar()
        self.priority = (max_priority or 0) + 1


        self.name = item["name"][0]
        self.notes = item["notes"][0]
        self.completed = False
        self.date_entered = datetime.datetime.now()
        self.date_completed = None


    def __repr__(self):
        item ={
            "id":self.id,
            # "item_priority":self.item_priority,
            "name":self.name,
            "notes":self.notes,
            "completed":self.completed,
            "date_entered":self.date_entered,
            "date_completed":self.date_completed
        }

        return item
