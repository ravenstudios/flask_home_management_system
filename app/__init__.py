from flask import Flask

from .todo_list.todo_list_blueprint import todo_list_blueprint
from .extensions import db


def create_app():
    app = Flask(__name__)
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///db.sqlite3"

    db.init_app(app)
    app.register_blueprint(todo_list_blueprint)
    return app

    # @app.route('/')
    # def index():
    #     return "<h1>No Blueprintes registerd</h1>"
# if __name__ == "__main__":
#     # from routes import *
#
#     # with app.app_context():
#     #     db.create_all()
#     app.run(debug=True)
#
#     # from waitress import serve
#     # serve(app, host="0.0.0.0", port=5005)
