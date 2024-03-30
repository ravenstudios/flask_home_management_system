from flask import redirect, url_for, render_template, request
from app.models.todo_model import Item
from app.models.messages_model import Message
from app.models.email_server_model import Email_server
import datetime
from app.extensions import db
from flask import Blueprint
from flask_login import login_required
from flask_mail import Message
from flask import current_app


email_server_blueprint = Blueprint('email_server_blueprint', __name__, template_folder='./templates', static_folder='static', url_prefix='/email-server')



@email_server_blueprint.route('send-email', methods = ['GET', 'POST'])
@login_required
def send_email():
    args = request.args

    title = args.get("subject")
    recipients = [args.get("recipients") + '@tmomail.net']
    content = args.get("content")

    msg = Message(
        subject,
        sender ='noreply@hms.hms',
        recipients = recipients
    )

    msg.body = content

    current_app.mail.send(msg)
    return redirect(request.referrer)






@email_server_blueprint.route('add-new-email-server-form', methods = ['GET', 'POST'])
@login_required
def add_new_email_server_form():

    email_server = Email_server.query.first()
    if not email_server:
        return render_template('email_server/add_new_email_server_form.html')
    else:
        return render_template('email_server/add_new_email_server_form.html', email_server=email_server)


@email_server_blueprint.route('add-new-email_server', methods = ['GET', 'POST'])
@login_required
def add_new_email_server():
    form_data = request.form.to_dict(flat=False)
    args = request.args
    email_server_id = args.get("email_server_id")

    if email_server_id:
        email_server = Email_server.query.get_or_404(email_server_id)
        email_server.server = request.form.get('server')
        email_server.port = request.form.get('port')
        email_server.username = request.form.get('username')
        email_server.password = request.form.get('password')
        db.session.add(email_server)
        db.session.commit()
        return redirect("/")

    else:

        email_server = Email_server(form_data)
        db.session.add(email_server)
        db.session.commit()
        return redirect("/")
