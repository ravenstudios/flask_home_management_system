from flask import Flask

from app.todo_list.todo_list_blueprint import todo_list_blueprint
from app.extensions import db
from app.config import Config

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)
    db.init_app(app)

    app.register_blueprint(todo_list_blueprint)


    
    return app
