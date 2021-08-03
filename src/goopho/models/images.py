from goopho.models import db

class Image(db.Model):

    __tablename__ = "image"

    id = db.Column(db.Integer, primary_key=True)
    
    name = db.Column(db.String(100))
    
    product_id = db.Column(db.Integer, db.ForeignKey('product.id'))

    def __init__(self, name, product_id):

        self.name = name
        
        self.product_id = product_id