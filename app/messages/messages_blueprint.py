from flask import redirect, url_for, render_template, request
from app.models.todo_model import Item
from app.models.messages_model import Message
from app.models.users_model import User
import datetime
from app.extensions import db, push_notification
from flask import Blueprint
from flask_login import login_required



messages_blueprint = Blueprint('messages_blueprint', __name__, template_folder='./templates', static_folder='static', url_prefix='/messages')



@messages_blueprint.route('/')
@login_required
def index():
    return render_template('messages/show_messages.html', messages=Message.query.all(), title="Messages")


@messages_blueprint.route('show-single-message')
@login_required
def show_single_message():
    id = request.args.get('id')
    return render_template('messages/show_single_message.html', message=Message.query.get(id))


@messages_blueprint.route('add-new-message-form', methods = ['GET', 'POST'])
@login_required
def add_new_message_form():
    return render_template('messages/add_new_message_form.html', users = User.query.all(), title="Messages")


@messages_blueprint.route('add-new-message', methods = ['GET', 'POST'])
@login_required
def add_new_message():
    form_data = request.form.to_dict(flat=False)
    user = User.query.filter_by(name=form_data["directed_to"][0]).first()
    message = Message(form_data)
    message.user_id = user.id

    push_notification(None, message.title, message.content)
    db.session.add(message)
    db.session.commit()
    return redirect("/messages")


@messages_blueprint.route('/delete-message', methods = ['GET'])
@login_required
def delete_item():
    args = request.args
    Message.query.filter_by(id=args.get("id")).delete()
    db.session.commit()
    return redirect("/messages")
