from app.extensions import db
import datetime



class User(db.Model):
    __tablename__ = "users"
    _id = db.Column(db.Integer, primary_key=True)

    name = db.Column(db.String(100))
    phone = db.Column(db.String(20))
    image_file_location = db.Column(db.String(300))

    messages = db.relationship("Message", backref="users")
    paychecks = db.relationship("Paycheck", backref="users")



    def __init__(self, user):
        self.name = user["name"][0]
        self.phone = user["phone"][0]
        


    def __repr__(self):
        user ={
            "_id":self._id,
            "name":self.name,
            "image_file_location":self.image_file_location
        }

        return user
