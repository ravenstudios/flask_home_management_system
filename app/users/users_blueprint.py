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

users_blueprint = Blueprint('users_blueprint', __name__, template_folder='./templates', static_folder='static', url_prefix='/users')




@users_blueprint.route('list-users')
def index():
    # return "<h1>users<?h1>"
    return render_template('users/list-users.html', users=User.query.all(), title="List Users")



@users_blueprint.route('add-new-user-form', methods = ['GET', 'POST'])
def add_new_user_form():
    return render_template('users/add-new-user-form.html', title="Add New User")




@users_blueprint.route('add-new-user', methods = ['GET', 'POST'])
def add_new_user():
    if request.method == 'POST':
        form_data = request.form.to_dict(flat=False)
        user = User(form_data)
        user.password = form_data["password_hash"][0]
        f = request.files['image_file_location']
        print(f"f:{f.filename}")
        user.image_file_location = f"/static/images/{f.filename}"
        f.save("app/static/images/" + f.filename)

        db.session.add(user)
        db.session.commit()
    return redirect("add-new-user-form")



@users_blueprint.route('add-new-paycheck-form', methods = ['GET', 'POST'])
def add_new_paycheck_form():
    return render_template('users/add_new_paycheck_form.html', title="Add New Paycheck", users = User.query.all())



@users_blueprint.route('add-new-paycheck', methods = ['GET', 'POST'])
def add_new_message():
    form_data = request.form.to_dict(flat=False)
    user = User.query.filter_by(name=form_data["user"][0]).first()
    # print(f"User:{user}")
    paycheck = Paycheck(form_data)
    paycheck.user_id = user._id
    db.session.add(paycheck)
    db.session.commit()
    return redirect("/users")
