import os

basedir = os.path.abspath(os.path.dirname(__file__))



import secrets


class Config:
    SECRET_KEY = secrets.token_hex(16)
    FLASK_DEBUG = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URI')\
        or 'sqlite:///' + os.path.join(basedir, 'db.sqlite3')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    UPLOADS_DEFAULT_DEST = "static/images"

    MAIL_SERVER = 'smtp.gmail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = 'ravenstudiosrob@gmail.com'
    MAIL_PASSWORD = 'hdbr kxba xtbo wpdc'
