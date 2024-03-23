from app.extensions import db
from sqlalchemy.orm import relationship
import datetime



class Bill(db.Model):
    __tablename__ = "bills"
    _id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    ammount = db.Column(db.Integer)
    notes = db.Column(db.String(100))
    date_due = db.Column(db.Date())
    date_paid = db.Column(db.Date())
    is_paid = db.Column(db.Boolean())


    def __init__(self, bill):
        self.name = bill.get("name", [""])[0]
        self.ammount = float(bill.get("ammount", [0])[0])
        self.notes = bill.get("notes", [""])[0]
        date = bill.get("date_due", [""])[0]
        self.date_due = datetime.datetime.strptime(date, '%Y-%m-%d').date()
        self.date_paid = None
        self.is_paid = False



    def __repr__(self):
        return {
            "_id":self._id,
            "name":self.name,
            "ammount":self.ammount,
            "notes":self.notes,
            "date_due":self.date_due,
            "date_paid":self.date_paid,
            "is_paid":self.is_paid,
        }



class Paycheck(db.Model):
    __tablename__ = "paychecks"
    _id = db.Column(db.Integer, primary_key=True)
    ammount = db.Column(db.Integer)
    notes = db.Column(db.String(100))
    date_paid = db.Column(db.Date())


    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    user = db.relationship("User", back_populates="paychecks")


    def __init__(self, paycheck):
        self.amount = float(paycheck.get("amount", [0])[0])
        self.notes = paycheck.get("notes", [""])[0]
        date = paycheck.get("date_paid", [""])[0]
        self.date_paid = datetime.datetime.strptime(date, '%Y-%m-%d').date()



    def __repr__(self):
        return {
            "_id":self._id,
            "name":self.name,
            "ammount":self.ammount,
            "notes":self.notes,
            "date_paid":self.date_paid,
        }
