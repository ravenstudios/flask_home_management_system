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
    # return "<h1>shopping_list<?h1>"
    return render_template('shopping_list/show_items.html', items=Shopping_list_item.query.all(), title="Shopping List Items")



@shopping_list_blueprint.route('add-new-item-form', methods = ['GET', 'POST'])
@login_required
def add_new_item_form():
    return render_template('shopping_list/add_new_item_form.html', title="Add New Shopping List Item")




@shopping_list_blueprint.route('add-new-item', methods = ['GET', 'POST'])
@login_required
def add_new_item():
    form_data = request.form.to_dict(flat=False)
    item = Shopping_list_item(form_data)
    db.session.add(item)
    db.session.commit()
    return redirect("/shopping-list")


@shopping_list_blueprint.route('delete-item', methods = ['GET', 'POST'])
@login_required
def delete_item():
    args = request.args
    Shopping_list_item.query.filter_by(id=args.get("id")).delete()
    db.session.commit()
    return redirect("/shopping-list")
