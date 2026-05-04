from app.extensions import db
import datetime



class Shopping_list_item(db.Model):
    __tablename__ = "shopping_list"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    date_entered = db.Column(db.Date())
    save_for_later = db.Column(db.Boolean())
    is_priority = db.Column(db.Boolean())


    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    user = db.relationship("User", back_populates="shopping_list")



    def __init__(self, item):
        self.name = item["name"][0]
        self.date_entered = datetime.datetime.now()
        self.is_priority = False
        self.save_for_later = False

    def __repr__(self):
        item ={
            "id":self.id,
            "name":self.name,
            "notes":self.notes,
            "date_entered":self.date_entered,
        }

        return item
