from goopho.models import db

class Image(db.Model):

    __tablename__ = "image"

    id = db.Column(db.Integer, primary_key=True)
    
    image = db.Column(db.String(100))
    
    product_id = db.Column(db.Integer, db.ForeignKey('product.id'))

    def __init__(self, image, product_id):

        self.image = image
        
        self.product_id = product_id