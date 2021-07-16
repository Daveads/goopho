from goopho.model import db
from sqlalchemy.sql import func

class Image(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    
    image_name = db.Column(db.String(100))
    
    product_id = db.Column(db.Integer, db.ForeignKey('product.id'))


