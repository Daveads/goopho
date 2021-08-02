from goopho.models import db
from sqlalchemy.sql import func

from datetime import datetime 

datenow = datetime.now()

class Product(db.Model):

    __tablename__ = "product"

    id = db.Column(db.Integer, primary_key=True)

    product_pub_id = db.Column(db.String(50), unique=True, nullable=False)
    
    title = db.Column(db.String(50), nullable=False)
    
    description = db.Column(db.String(1000), nullable=False)
    
    created_on = db.Column(db.String(20), nullable=False)

    user_pub_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    
    isAvailable = db.Column(db.Boolean, default=True)
    
    isDeleted = db.Column(db.Boolean, default=False)
    
    images = db.relationship('Image', backref='product')

    
    def __init__(self, title, description, user_pub_id, product_pub_id):

        self.title = title
        self.description = description
        self.user_pub_id = user_pub_id
        self.created_on = datenow.strftime("%d/%m/%Y %H:%M:%S")
        self.product_pub_id = product_pub_id
