from flask import redirect
from flask import url_for
from flask import render_template
from flask import request, flash
from app.models.todo_model import Item
from app.models.messages_model import Message
from app.models.finances_model import Bill, Paycheck
from app.models.users_model import User
import datetime
from app.extensions import db
from flask import Blueprint
from flask_login import login_required



users_blueprint = Blueprint('users_blueprint', __name__, template_folder='./templates', static_folder='static', url_prefix='/users')



@users_blueprint.route('/')
@users_blueprint.route('user-dashboard')
@login_required
def user_dashboard():
    # return "<h1>users<?h1>"
    return render_template('users/user-dashboard.html')



@users_blueprint.route('list-users')
@login_required
def list_users():
    # return "<h1>users<?h1>"
    return render_template('users/list-users.html', users=User.query.all(), title="List Users")





@users_blueprint.route('change-password-form')
@login_required
def change_password_form():
    user = User.query.get(request.args.get("id"))
    return render_template('users/change-password-form.html', user=user, title="Change Password")


@users_blueprint.route('/change-password', methods=['POST'])
@login_required
def change_password():
    user_id = request.form.get("id")
    current_password = request.form.get("current-password")
    new_password = request.form.get("new-password")
    confirm_password = request.form.get("confirm-password")

    user = User.query.get(user_id)

    if user is None:
        flash("User not found")
        return redirect("/users")

    if not user.verify_password(current_password):
        flash("Current password is incorrect")
        return redirect(f"/users/change-password-form?id={user.id}")

    if new_password != confirm_password:
        flash("New passwords do not match")
        return redirect(f"/users/change-password-form?id={user.id}")

    if len(new_password) < 4:
        flash("Password must be at least 4 characters")
        return redirect(f"/users/change-password-form?id={user.id}")

    user.password = new_password
    db.session.commit()

    flash("Password changed successfully")
    return redirect("/users")


@users_blueprint.route('change-icon-form')
@login_required
def change_icon():
    user = User.query.get(request.args.get("id"))
    return render_template('users/change-icon-form.html', users=user, title="Change Icon")




@users_blueprint.route('add-new-user-form', methods = ['GET', 'POST'])
@login_required
def add_new_user_form():
    return render_template('users/add-new-user-form.html', title="Add New User")





@users_blueprint.route('delete-user', methods = ['GET', 'POST'])
@login_required
def delete_user():
    args = request.args
    user_id = args.get("id")
    user = User.query.get(user_id)

    if user is None:
        flash("User not found.", "error")
        return redirect("/users")
    else:
        db.session.delete(user)
        db.session.commit()
        flash("User deleted successfully.", "success")
        return redirect("/users")




@users_blueprint.route('edit-user-form', methods = ['GET', 'POST'])
@login_required
def edit_user_form():
    args = request.args
    user = User.query.filter_by(id=args.get("id")).first()
    return render_template('users/edit-user-form.html', title="Edit User", user=user)




@users_blueprint.route('edit-user', methods = ['GET', 'POST'])
@login_required
def edit_user():
    if request.method == 'POST':
        form_data = request.form.to_dict(flat=False)
        user = User.query.filter_by(id=form_data["id"][0]).first()

        if form_data["name"][0]:
            user.name = form_data["name"][0]
        if form_data["username"][0]:
            user.username = form_data["username"][0]
        if form_data["push_device"][0]:
            user.push_device = form_data["push_device"][0]

        user.privilege = form_data["privilege"][0]

        if request.files['image_file_location']:
            user_image_file = request.files['image_file_location']
            user.image_file_location = f"/static/images/{user_image_file.filename}"
            user_image_file.save("app/static/images/" + user_image_file.filename)

        db.session.add(user)
        db.session.commit()
    return redirect("/users")



@users_blueprint.route('add-new-user', methods = ['GET', 'POST'])
@login_required
def add_new_user():
    if request.method == 'POST':
        form_data = request.form.to_dict(flat=False)
        user = User(form_data)
        user.password = form_data["password"][0]
        print(user.password_hash)
        user_image_file = request.files['image_file_location']
        user.image_file_location = f"/static/images/{user_image_file.filename}"
        user_image_file.save("app/static/images/" + user_image_file.filename)

        db.session.add(user)
        db.session.commit()
    return redirect("/users")
