from flask import redirect
from flask import url_for
from flask import render_template
from flask import request
from app.models.todo_model import Item
import datetime
from app.extensions import db
from flask import Blueprint
from flask_login import login_required


todo_list_blueprint = Blueprint('todo_list_blueprint', __name__, template_folder='templates', static_folder='static', url_prefix='/todo_list')




@todo_list_blueprint.route('/')
@login_required
def index():
    return render_template('todo_list/show_items.html', items=Item.query.order_by(Item.item_priority).all(), title="Todo List")



@todo_list_blueprint.route('/add-new-item-form', methods = ['GET', 'POST'])
@login_required
def add_new_item_form():

    id = request.args.get('_id')
    if id:
        return render_template('todo_list/add_new_item_form.html', item=Item.query.get(id))
    else:
        return render_template('todo_list/add_new_item_form.html')


@todo_list_blueprint.route('/add-new-item', methods = ['GET', 'POST'])
@login_required
def add_new_item():
    form_data = request.form.to_dict(flat=False)
    item = Item(form_data)


    db.session.add(item)
    db.session.commit()
    return redirect("/todo_list")


@todo_list_blueprint.route('/delete-item', methods = ['GET'])
@login_required
def delete_item():
    args = request.args
    Item.query.filter_by(_id=args.get("_id")).delete()
    db.session.commit()
    return redirect("/todo_list")


@todo_list_blueprint.route('/toggle-completed', methods = ['GET'])
@login_required
def toggle_completed():
    id = request.args.get('_id')
    item=Item.query.get(id)
    checked = request.args.get('checked')

    if checked == "true":
        item.item_completed = True
    else:
        item.item_completed = False
    db.session.commit()
    return redirect("/todo_list")



@todo_list_blueprint.route('/change-item-priority-up', methods = ['GET'])
@login_required
def change_item_priority_up():
    item_id = request.args.get('_id', type=int)

    item_to_move = Item.query.get(item_id)
    item_to_swap = Item.query.get(item_id - 1)
    if item_to_move and item_to_swap:
        item_to_move.item_priority, item_to_swap.item_priority = item_to_swap.item_priority, item_to_move.item_priority
        db.session.commit()
    return redirect("/todo_list")


@todo_list_blueprint.route('/change-item-priority-down', methods = ['GET'])
@login_required
def change_item_priority_down():
    item_id = request.args.get('_id', type=int)

    item_to_move = Item.query.get(item_id)
    item_to_swap = Item.query.get(item_id + 1)
    if item_to_move and item_to_swap:
        item_to_move.item_priority, item_to_swap.item_priority = item_to_swap.item_priority, item_to_move.item_priority
        db.session.commit()
    return redirect("/todo_list")
