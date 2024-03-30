from flask_sqlalchemy import SQLAlchemy
from flask_mail import Message
from flask import current_app


db = SQLAlchemy()


def push_notification(user, title, content):
    import requests

    url = 'https://api.pushover.net/1/messages.json'
    myobj = {
        "device":"Robs_iPhone",
        "title": title,
        "token": "amqde3o6om81ai33kvvtar84pozhse",
        "user": "ujvr6a8zzjm2jii6v71eivgcrg1zn3",
        "message": content,
        "sound":"alien",
        }

    x = requests.post(url, json = myobj)
    print(x)
