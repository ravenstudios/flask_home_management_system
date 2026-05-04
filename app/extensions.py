from flask_sqlalchemy import SQLAlchemy

#

db = SQLAlchemy()


def push_notification(push_device, title, content):
    import requests

    url = 'https://api.pushover.net/1/messages.json'
    myobj = {
        "device":push_device,
        "title": title,
        "token": "amqde3o6om81ai33kvvtar84pozhse",
        "user": "ujvr6a8zzjm2jii6v71eivgcrg1zn3",
        "message": content,
        "sound":"alien",
        }

    x = requests.post(url, json = myobj)


def reset_chores(app):

    with app.app_context():
        from app.models.chores_model import Chore
        chores_to_update = Chore.query.filter(Chore.completed == True, Chore.repeated == True).all()
        for chore in chores_to_update:
            chore.completed = False

        db.session.commit()
