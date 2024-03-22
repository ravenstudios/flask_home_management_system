from flask import redirect
from flask import url_for
from flask import render_template
from flask import request
from app.models.todo_model import Item
from app.models.messages_model import Message
from app.models.users_model import User
import datetime
from app.extensions import db
from flask import Blueprint

messages_blueprint = Blueprint('messages_blueprint', __name__, template_folder='./templates', static_folder='static', url_prefix='/messages')




@messages_blueprint.route('/')
def index():
    # return "<h1>messages<?h1>"
    return render_template('messages/show_messages.html', messages=Message.query.all(), title="Messages")


@messages_blueprint.route('show-single-message')
def show_single_message():
    # return "<h1>messages<?h1>"
    id = request.args.get('_id')
    return render_template('messages/show_single_message.html', message=Message.query.get(id))


@messages_blueprint.route('add-new-message-form', methods = ['GET', 'POST'])
def add_new_message_form():
    # return "!!!!!!!!!!!!!!!"
    # id = request.args.get('_id')
    # if id:
    #     return render_template('messages/add_new_message_form.html', item=Item.query.get(id))
    # else:
    return render_template('messages/add_new_message_form.html', users = User.query.all())


@messages_blueprint.route('add-new-message', methods = ['GET', 'POST'])
def add_new_item():
    form_data = request.form.to_dict(flat=False)
    message = Message(form_data)
    db.session.add(message)
    db.session.commit()
    return redirect("/messages")


@messages_blueprint.route('/delete-message', methods = ['GET'])
def delete_item():
    args = request.args
    Message.query.filter_by(_id=args.get("_id")).delete()
    db.session.commit()
    return redirect("/messages")
#
#
# @messages_blueprint.route('/toggle-completed', methods = ['GET'])
# def toggle_completed():
#     id = request.args.get('_id')
#     item=Item.query.get(id)
#     checked = request.args.get('checked')
#
#     if checked == "true":
#         item.item_completed = True
#     else:
#         item.item_completed = False
#     db.session.commit()
#     return redirect("/todo")
#
#
#
# @messages_blueprint.route('/change-item-priority-up', methods = ['GET'])
# def change_item_priority_up():
#     item_id = request.args.get('_id', type=int)
#
#     item_to_move = Item.query.get(item_id)
#     item_to_swap = Item.query.get(item_id - 1)
#     if item_to_move and item_to_swap:
#         item_to_move.item_priority, item_to_swap.item_priority = item_to_swap.item_priority, item_to_move.item_priority
#         db.session.commit()
#     return redirect(url_for('index'))
#
#
# @messages_blueprint.route('/change-item-priority-down', methods = ['GET'])
# def change_item_priority_down():
#     item_id = request.args.get('_id', type=int)
#
#     item_to_move = Item.query.get(item_id)
#     item_to_swap = Item.query.get(item_id + 1)
#     if item_to_move and item_to_swap:
#         item_to_move.item_priority, item_to_swap.item_priority = item_to_swap.item_priority, item_to_move.item_priority
#         db.session.commit()
#     return redirect(url_for('index'))
