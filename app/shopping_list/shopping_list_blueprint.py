from flask import redirect
from flask import render_template
from flask import request
from app.models.shopping_list_model import Shopping_list_item
from app.models.users_model import User
from app.extensions import db
from flask import Blueprint
from flask_login import login_required


shopping_list_blueprint = Blueprint('shopping_list_blueprint', __name__, template_folder='./templates', static_folder='static', url_prefix='/shopping-list')


@shopping_list_blueprint.route('/')
@login_required
def index():

    return render_template('shopping_list/show_items.html', items=Shopping_list_item.query.all(), title="Shopping List Items")



@shopping_list_blueprint.route('add-new-item-form', methods = ['GET', 'POST'])
@login_required
def add_new_item_form():
    return render_template('shopping_list/add_new_item_form.html', title="Add New Shopping List Item", users = User.query.all())




@shopping_list_blueprint.route('add-new-item', methods = ['GET', 'POST'])
@login_required
def add_new_item():
    form_data = request.form.to_dict(flat=False)
    item = Shopping_list_item(form_data)


    user = User.query.filter_by(name=form_data["user"][0]).first()
    item.user_id = user.id



    db.session.add(item)
    db.session.commit()
    return redirect("/shopping-list")


@shopping_list_blueprint.route('delete-items', methods = ['GET', 'POST'])
@login_required
def delete_items():
    args = request.args
    ids_string = args.get("ids")

    ids = list(map(int, ids_string.split(',')))

    # Delete rows with IDs in the list
    db.session.query(Shopping_list_item).filter(Shopping_list_item.id.in_(ids)).delete(synchronize_session=False)



    Shopping_list_item.query.filter_by(id=args.get("id")).delete()
    db.session.commit()
    return redirect("/shopping-list")


@shopping_list_blueprint.route('save-for-later', methods = ['GET', 'POST'])
@login_required
def save_for_later():
    args = request.args
    item = Shopping_list_item.query.get(args.get("id"))
    item.save_for_later = True if args.get("state") == "True" else False
    db.session.add(item)
    db.session.commit()
    return redirect("/shopping-list")



@shopping_list_blueprint.route('is-priority', methods = ['GET', 'POST'])
@login_required
def is_priority():
    args = request.args
    item = Shopping_list_item.query.get(args.get("id"))
    item.is_priority = True if args.get("state") == "True" else False
    db.session.add(item)
    db.session.commit()
    return redirect("/shopping-list")
