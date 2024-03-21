from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import datetime


app = Flask(__name__, static_url_path='/static')
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///bills.sqlite3"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)





if __name__ == "__main__":
    from routes import *

    with app.app_context():
        db.create_all()
    app.run(debug=True)

    # from waitress import serve
    # serve(app, host="0.0.0.0", port=5005)
