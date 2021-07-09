from goopho.model import db
from sqlalchemy.sql import func

class Product(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    
    small_description = db.Column(db.String(300), nullable=False)
    
    long_description = db.Column(db.String(1000), nullable=True)
    
    created_on = db.Column(db.DateTime(timezone=True), default=func.now())

    user_pub_id = db.Column(db.Integer, db.ForeignKey('user.public_id'))
    
    images = db.relationship('Image')

    
