from flask import redirect
from flask import url_for
from flask import render_template
from flask import request
from app.models.todo_model import Item
from app.models.messages_model import Message
from app.models.finances_model import Bill, Paycheck
from app.models.users_model import User
import datetime
from app.extensions import db
from flask import Blueprint
from flask_login import login_required


finances_blueprint = Blueprint('finances_blueprint', __name__, template_folder='./templates', static_folder='static', url_prefix='/finances')


@finances_blueprint.route('/show-paychecks')
@finances_blueprint.route('/')
@login_required
def show_paychecks():
    return render_template('finances/show_paychecks.html', paychecks=Paycheck.query.all(), title="Paychecks")


@finances_blueprint.route('/show-bills')
@login_required
def show_bills():
    return render_template('finances/show_bills.html', bills=Bill.query.all(), title="Bills")



@finances_blueprint.route('add-new-bill-form', methods = ['GET', 'POST'])
@login_required
def add_new_bill_form():
    return render_template('finances/add_new_bill_form.html', title="Add New Bill", paychecks=Paycheck.query.all())




@finances_blueprint.route('add-new-bill', methods = ['GET', 'POST'])
@login_required
def add_new_bill():
    form_data = request.form.to_dict(flat=False)
    bill = Bill(form_data)
    # get paycheck id
    paycheck = Paycheck.query.filter_by(id=form_data["paycheck_id"][0]).first()

    bill.paycheck_id = paycheck.id

    db.session.add(bill)
    db.session.commit()
    return render_template('finances/add_new_bill_form.html', title="Add New Bill", paychecks=Paycheck.query.all())



@finances_blueprint.route('add-new-paycheck-form', methods = ['GET', 'POST'])
@login_required
def add_new_paycheck_form():
    return render_template('finances/add_new_paycheck_form.html', title="Add New Paycheck", users = User.query.all())



@finances_blueprint.route('add-new-paycheck', methods = ['GET', 'POST'])
@login_required
def add_new_message():
    form_data = request.form.to_dict(flat=False)
    user = User.query.filter_by(name=form_data["user"][0]).first()
    # print(f"User:{user}")
    paycheck = Paycheck(form_data)
    paycheck.user_id = user.id
    db.session.add(paycheck)
    db.session.commit()
    return redirect("/finances")
