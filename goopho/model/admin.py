from goopho.model import db

class Admin(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    public_id = db.Column(db.String(50), unique=True) 
    name = db.Column(db.String(50))
    email = db.Column(db.String(50))
