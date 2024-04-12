from app.extensions import db
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from app.models.chores_model import Chore


class User(db.Model, UserMixin):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    username = db.Column(db.String(100))
    password_hash = db.Column(db.String(128))
    push_device = db.Column(db.String(20))
    image_file_location = db.Column(db.String(300))
    privilege = db.Column(db.Integer, default=0)#    0:user, 1:elevated, 2:admin
    messages = db.relationship("Message", back_populates="user")
    shopping_list = db.relationship("Shopping_list_item", back_populates="user")

    paychecks = db.relationship("Paycheck", back_populates="user")
    chores = db.relationship("Chore", back_populates="user", foreign_keys=[Chore.user_id])

    chores_created = db.relationship("Chore", back_populates="from_user", foreign_keys=[Chore.from_user_id])
    todo_list = db.relationship("Item", back_populates="user")

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
        self.push_device = user["push_device"][0]
        self.username = user["username"][0]

    def __repr__(self):
        user ={
            "id":self.id,
            "name":self.name,
            "image_file_location":self.image_file_location
        }

        return user
