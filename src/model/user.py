from config.db import db, app, ma 

class user(db.Model):
    __tablename__ = "tbluser"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    lastname = db.Column(db.String(50))
    producto = db.Column(db.Integer,db.ForeignKey("tblproduct.id"))


    def __init__(self, name, lastname, message):
        self.name = name
        self.lastname = lastname
        self.message = message

with app.app_context():
    db.create_all() 