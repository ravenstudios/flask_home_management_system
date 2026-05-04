from app.extensions import db



class Email_server(db.Model):
    __tablename__ = "email_server"
    id = db.Column(db.Integer, primary_key=True)
    server = db.Column(db.String(100))
    port = db.Column(db.String(100))
    username = db.Column(db.String(100))
    password = db.Column(db.String(100))




    def __init__(self, email_server):
        self.server = email_server["server"][0]
        self.port = email_server["port"][0]
        self.username = email_server["username"][0]
        self.password = email_server["password"][0]






    def __repr__(self):
        email_server ={
            "id":self.id,
            "server":self.server,
            "port":self.port,
            "username":self.username,
            "password":self.password,
        }

        return email_server
