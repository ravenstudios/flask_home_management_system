from flask import redirect
from flask import url_for
from flask import render_template
from flask import request
from app.models.chores_model import Chore
from datetime import datetime
from app.extensions import db, push_notification
from flask import Blueprint
from flask_login import login_required
from app.models.users_model import User
from flask import current_app



chores = Blueprint('chores', __name__, template_folder='templates', static_folder='static', url_prefix='/chores')




@chores.route('/')
@login_required
def index():
    return render_template('chore_list/show-chores.html', chores=Chore.query.all(), title="Show Chores")



@chores.route('/add-new-chore-form', methods = ['GET', 'POST'])
@login_required
def add_new_chore_form():

    id = request.args.get("id")
    users = User.query.all()

    if id:
        return render_template('chore_list/add-new-chore-form.html', users=users, chore=Chore.query.get(id), title="Edit Chore")
    else:
        users = User.query.all()
        return render_template('chore_list/add-new-chore-form.html', users=users, title="Add New Chore")




@chores.route('/complete-chore-form', methods = ['GET', 'POST'])
@login_required
def complete_chore_form():
    args = request.args
    id=args.get("id")
    chore = Chore.query.get(id)
    return render_template('chore_list/complete-chore-form.html', chore=chore)



@chores.route('/complete-chore', methods = ['GET', 'POST'])
@login_required
def complete_chore():
    args = request.args
    id=args.get("id")
    chore = Chore.query.get(id)


    form_data = request.form.to_dict(flat=False)
# <<<<<<< HEAD
    user = User.query.filter_by(name=form_data["directed_to"][0]).first()
    chore = Chore(form_data)
    chore.user_id = user.id
# =======
    # append Notes
    new_notes = form_data.get("notes")[0]
    new_notes += "\n"
    new_notes += "".join(chore.notes)
    chore.notes = new_notes
    # set date_completed
    chore.date_completed = datetime.now()

    # mark completed
    chore.completed = True
    # send copy of completed chore to parents

    new_chore = Chore(
        {
            "name":["COMPLETED: " + chore.name],
            "notes":[chore.notes],
            "completed":[False],
            "date_entered":[chore.date_entered],
            "repeat_time":[chore.repeat_time],
        }
    )

    new_chore.repeat = chore.repeat
    new_chore.user_id = chore.from_user_id
    new_chore.from_user_id = chore.user_id
    # push to parents

    message = f"Chore: {chore.name} completed"
    conent = f"Completed at {datetime.now()}"
    push_notification(
        chore.from_user.push_device,
        message,
        conent
    )


    db.session.add(chore)
    db.session.add(new_chore)
    db.session.commit()
    return redirect("/chores")
    # return render_template('chore_list/complete-chore-form.html', chore=chore)




@chores.route('/add-new-chore', methods = ['GET', 'POST'])
@login_required
def add_new_chore():
    form_data = request.form.to_dict(flat=False)
    # to_user = User.query.get(id=form_data["to_user"][0])
    # from_user = User.query.get(id=form_data["from_user"][0])



    id = request.args.get("id")

    if id:
        chore=Chore.query.get(id)
        chore.name = form_data.get("name")[0]
        chore.notes = form_data.get("notes")[0]
        # chore.repeat = form_data.get("repeat")
        chore.repeat_time = form_data.get("repeat_time")[0]

        chore.repeat = True if "repeat" in form_data else False
        chore.user_id = form_data.get("to_user")[0]
        chore.from_user_id = form_data.get("from_user")[0]
        db.session.add(chore)
        db.session.commit()
        return redirect("/chores")
    else:
        chore = Chore(form_data)
        chore.user_id = form_data.get("to_user")[0]
        chore.from_user_id = form_data.get("from_user")[0]
        chore.repeat = True if "repeat" in form_data else False
        db.session.add(chore)
        db.session.commit()
        return redirect("/chores")


@chores.route('show-chore')
@login_required
def show_single_chore():
    id = request.args.get('id')
    return render_template('chore_list/show-chore.html', chore=Chore.query.get(id))


@chores.route('un-complete-chore')
@login_required
def uncomplete_chore():
    chore = Chore.query.get(request.args.get('id'))
    chore.completed = False
# >>>>>>> origin
    db.session.add(chore)
    db.session.commit()
    return redirect("/chores")




@chores.route('/delete-chore', methods = ['GET'])
@login_required
def delete_chore():
    args = request.args
    Chore.query.filter_by(id=args.get("id")).delete()
    db.session.commit()
    return redirect("/chores")
