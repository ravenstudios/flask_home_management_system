from flask import redirect, url_for, render_template, request, flash
from flask import Blueprint
from flask_login import login_required, login_user, logout_user
from app.models.users_model import User
from app.extensions import db


login_blueprint = Blueprint('login_blueprint', __name__, template_folder='./templates', static_folder='static')




@login_blueprint.route('/login-form')
@login_blueprint.route('/')
def login_form():
    user = User.query.first()
    if not user:
        admin_user = {
            "name": ["admin"],
            "username": ["admin"],
            "push_device": "Robs_iPhone",
        }


        new_user = User(admin_user)
        new_user.image_file_location =  "/static/images/admin.png"
        new_user.privilege = 2

        db.session.add(new_user)
        db.session.commit()
    return render_template('login/login-form.html')


@login_blueprint.route('/login',  methods = ['POST'])
def login():
    if request.method == 'POST':
        form_data = request.form.to_dict(flat=False)
        user = User.query.filter_by(username=form_data["username"][0]).first()
        password = "pw"
        if user:
             if password:
                 login_user(user, remember=True)
                 flash("Logged In")
                 return redirect('/users/user-dashboard')

        else:
            flash("Logged In Error")
            return redirect('/login-form')


@login_blueprint.route('/logout',  methods = ['GET', 'POST'])
@login_required
def logout():
    logout_user()
    flash("Logged Out")
    return render_template('login/login-form.html')
