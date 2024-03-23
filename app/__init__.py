from flask import Flask
from flask_migrate import Migrate

from app.todo_list.todo_list_blueprint import todo_list_blueprint
from app.messages.messages_blueprint import messages_blueprint


from app.extensions import db
from app.config import Config

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)
    db.init_app(app)

        # Create all database tables
    with app.app_context():
        db.create_all()

    migrate = Migrate(app, db)
    app.register_blueprint(todo_list_blueprint)
    app.register_blueprint(messages_blueprint)



    return app
