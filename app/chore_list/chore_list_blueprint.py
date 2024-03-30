from flask import redirect
from flask import url_for
from flask import render_template
from flask import request
from app.models.chores_model import Chore
import datetime
from app.extensions import db
from flask import Blueprint
from flask_login import login_required
from app.models.users_model import User

chores = Blueprint('chores', __name__, template_folder='templates', static_folder='static', url_prefix='/chores')




@chores.route('/')
@login_required
def index():
    return render_template('chore_list/show_items.html', chores=Chore.query.all(), title="Chore List")



@chores.route('/add-new-item-form', methods = ['GET', 'POST'])
@login_required
def add_new_item_form():
    users = User.query.all()
    return render_template('chore_list/add_new_item_form.html', users=users)


@chores.route('/add-new-item', methods = ['GET', 'POST'])
@login_required
def add_new_item():
    form_data = request.form.to_dict(flat=False)
    chore = Chore(form_data)

    user = User.query.filter_by(name=form_data["user"][0]).first()

    chore.user_id = user.id

    db.session.add(chore)
    db.session.commit()
    return redirect("/chores")



@chores.route('show-chore')
@login_required
def show_single_chore():
    id = request.args.get('id')
    return render_template('chore_list/show_chore.html', chore=Chore.query.get(id))



@chores.route('/delete-item', methods = ['GET'])
@login_required
def delete_item():
    args = request.args
    Chore.query.filter_by(id=args.get("id")).delete()
    db.session.commit()
    return redirect("/chores")

@chores.route('/complete-item', methods = ['GET'])
@login_required
def complete_item():
    args = request.args
    Chore.query.filter_by(id=args.get("id")).complete()
    db.session.commit()
    return redirect("/chores")
