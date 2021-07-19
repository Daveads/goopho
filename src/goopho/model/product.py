from goopho.model import db
from sqlalchemy.sql import func

class Product(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    
    title = db.Column(db.String(50), nullable=False)
    
    description = db.Column(db.String(1000), nullable=True)
    
    created_on = db.Column(db.DateTime(timezone=True), default=func.now())

    user_pub_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    
    images = db.relationship('Image')

    
