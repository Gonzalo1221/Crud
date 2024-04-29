from config.db import db, app, ma 

class user(db.Model):
    __tablename__ = "tbluser"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    lastname = db.Column(db.String(50))
    phone = db.Column(db.String(50))
    product = db.Column(db.Integer,db.ForeignKey("tblproduct.id"))


    def __init__(self, name, lastname,phone , product):
        self.name = name
        self.lastname = lastname
        self.phone = phone
        self.product = product

with app.app_context():
    db.create_all()
class userSchema(ma.Schema):
        class Meta:
            fields = ('id', 'name', 'lastname','phone' ,'product')