from goopho.models import db
from sqlalchemy.sql import func
import datetime

class Product(db.Model):

    __tablename__ = "product"

    id = db.Column(db.Integer, primary_key=True)
    
    title = db.Column(db.String(50), nullable=False)
    
    description = db.Column(db.String(1000), nullable=False)
    
    created_on = db.Column(db.DateTime(timezone=True), nullable=False)

    user_pub_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    
    images = db.relationship('Image', backref='product')

    
    def __init__(self, title, description, user_pub_id):

        self.title = title
        self.description = description
        self.user_pub_id = user_pub_id
        self.created_on = datetime.datetime.now()
