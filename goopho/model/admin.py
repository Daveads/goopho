from goopho.model import db

class Admin(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    public_id = db.Column(db.String(50), unique=True) 
    email = db.Column(db.String(50))
    first_name = db.Column(db.String(50))
    last_name =	db.Column(db.String(50))
    password = db.Column(db.String(25))

