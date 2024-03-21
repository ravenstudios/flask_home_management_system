from __main__ import db
import datetime



class Item(db.Model):
    __tablename__ = "todo_list"
    _id = db.Column(db.Integer, primary_key=True)
    item_priority = db.Column(db.Integer)
    item_name = db.Column(db.String(100))
    item_notes = db.Column(db.String(300))
    item_completed = db.Column(db.Boolean())
    item_date_entered = db.Column(db.Date())
    item_date_completed = db.Column(db.Date())




    def __init__(self, item):
         # Auto-increment item_priority based on existing priorities
        max_priority = db.session.query(db.func.max(Item.item_priority)).scalar()
        self.item_priority = (max_priority or 0) + 1


        self.item_name = item["item_name"][0]
        self.item_notes = item["item_notes"][0]
        self.item_completed = False
        self.item_date_entered = datetime.datetime.now()
        self.item_date_completed = None


    def __repr__(self):
        item ={
            "_id":self._id,
            # "item_priority":self.item_priority,
            "item_name":self.item_name,
            "item_notes":self.item_notes,
            "item_completed":self.item_completed,
            "item_date_entered":self.item_date_entered,
            "item_date_completed":self.item_date_completed
        }

        return item
