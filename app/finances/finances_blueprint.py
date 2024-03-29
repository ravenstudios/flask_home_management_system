from flask import redirect
from flask import url_for
from flask import render_template
from flask import request
from app.models.todo_model import Item
from app.models.messages_model import Message
from app.models.finances_model import Bill, Paycheck
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
    today = datetime.date.today().isoformat()
    args = request.args
    bill_id = args.get("bill_id")
    if bill_id:
        bill = Bill.query.get_or_404(bill_id)
        return render_template(
            'finances/add_new_bill_form.html',
            title="Edit Bill",
            paychecks=Paycheck.query.all(),
            bill=bill,
            today=today
        )

    else:
        paycheck_id = request.args.get('paycheck_id')
        return render_template(
            'finances/add_new_bill_form.html',
            title="Add New Bill",
            paychecks=Paycheck.query.all(),
            paycheck_id=paycheck_id,
            today=today
        )




@finances_blueprint.route('add-new-bill', methods = ['GET', 'POST'])
@login_required
def add_new_bill():

    args = request.args
    bill_id = args.get("bill_id")
    form_data = request.form.to_dict(flat=False)
    paycheck = Paycheck.query.filter_by(id=form_data["paycheck_id"][0]).first()

    if bill_id:
        bill = Bill.query.get_or_404(bill_id)
        bill.name = request.form.get('name')
        bill.ammount = request.form.get('ammount')
        bill.notes = request.form.get('notes')
        bill.date_due = datetime.datetime.strptime(request.form.get('date_due'), '%Y-%m-%d').date()
        bill.date_paid = datetime.datetime.strptime(request.form.get('date_paid'), '%Y-%m-%d').date() if request.form.get('date_paid') else None
        bill.is_paid = True if request.form.get('is_paid') == 'on' else False
        bill.paycheck_id = paycheck.id
        db.session.add(bill)
        db.session.commit()
        return redirect("show-paychecks")

    else:
        bill = Bill(form_data)
        bill.paycheck_id = paycheck.id
        db.session.add(bill)
        db.session.commit()
        return render_template(
            'finances/add_new_bill_form.html',
            title="Add New Bill",
            paychecks=Paycheck.query.all()
        )


@finances_blueprint.route('/delete-bill', methods = ['GET'])
@login_required
def delete_item():
    args = request.args
    Bill.query.filter_by(id=args.get("bill_id")).delete()
    db.session.commit()
    return redirect("show-paychecks")



@finances_blueprint.route('add-new-paycheck-form', methods = ['GET', 'POST'])
@login_required
def add_new_paycheck_form():
    today = datetime.date.today().isoformat()
    return render_template(
        'finances/add_new_paycheck_form.html',
         title="Add New Paycheck",
         users = User.query.all(),
         today=today
    )



@finances_blueprint.route('add-new-paycheck', methods = ['GET', 'POST'])
@login_required
def add_new_message():
    form_data = request.form.to_dict(flat=False)
    user = User.query.filter_by(name=form_data["user"][0]).first()
    paycheck = Paycheck(form_data)
    paycheck.user_id = user.id
    db.session.add(paycheck)
    db.session.commit()
    return redirect("/finances")
