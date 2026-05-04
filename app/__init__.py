from flask import Flask
from flask_migrate import Migrate
from flask_login import LoginManager
from apscheduler.schedulers.background import BackgroundScheduler

from app.models.users_model import User
from app.extensions import db, reset_chores
from app.config import Config


def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    db.init_app(app)

    with app.app_context():
        db.create_all()

    migrate = Migrate(app, db, render_as_batch=True)

    # Import blueprints INSIDE create_app to avoid circular imports
    from app.todo_list.todo_list_blueprint import todo_list_blueprint
    from app.messages.messages_blueprint import messages_blueprint
    from app.finances.finances_blueprint import finances_blueprint
    from app.users.users_blueprint import users_blueprint
    from app.login.login_blueprint import login_blueprint
    from app.shopping_list.shopping_list_blueprint import shopping_list_blueprint
    from app.chore_list.chore_list_blueprint import chores

    app.register_blueprint(todo_list_blueprint)
    app.register_blueprint(messages_blueprint)
    app.register_blueprint(finances_blueprint)
    app.register_blueprint(users_blueprint)
    app.register_blueprint(login_blueprint)
    app.register_blueprint(shopping_list_blueprint)
    app.register_blueprint(chores)

    login_manager = LoginManager()
    login_manager.init_app(app)
    login_manager.login_view = "login_blueprint.login_form"

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id)) or None

    scheduler = BackgroundScheduler()
    scheduler.add_job(reset_chores, 'cron', hour=21, minute=0, args=[app])
    scheduler.start()

    return app
