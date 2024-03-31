from app.extensions import db
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin

class User(db.Model, UserMixin):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100))
    password_hash = db.Column(db.String(128))
    name = db.Column(db.String(100))
    phone = db.Column(db.String(20))
    image_file_location = db.Column(db.String(300))
    privilege = db.Column(db.Integer, default=0)#    0:user, 1:elevated, 2:admin
    messages = db.relationship("Message", back_populates="user")
    chores = db.relationship("Chore", back_populates="user")

    paychecks = db.relationship("Paycheck", back_populates="user")
    # shopping_list_item_requests = db.relationship("Shopping_list", back_populates="users")

    @property
    def password(self):
        raise AttributeError("Password is not a readable attribute")

    @password.setter
    def password(self, password):
        print(f"password:{password}")
        self.password_hash = generate_password_hash(password, method='pbkdf2:sha256')

    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)

    def __init__(self, user):
        self.name = user["name"][0]
        self.phone = user["phone"][0]
        self.username = user["username"][0]


    def __repr__(self):
        user ={
            "id":self._id,
            "name":self.name,
            "image_file_location":self.image_file_location
        }

        return user
