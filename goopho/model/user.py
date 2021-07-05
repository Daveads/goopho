from goopho.model import db
from sqlalchemy.sql import func
import enum 

class setRole(enum.Enum):
    user = "User"
    admin = "Admin"
    special = "Special"


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)

    public_id = db.Column(db.String(50), unique=True)

    name = db.Column(db.String(50))

    username = db.Column(db.String(50))
    
    email = db.Column(db.String(50))

    password = db.Column(db.String(200))

    roles = db.Column(db.Enum(setRole), default=setRole.user, nullable=False)
    
    acct_create_at = db.Column(db.DateTime(timezone=True), default=func.now())

    updated_at = db.Column(db.DateTime(timezone=True), default=func.now())
    
    email_verfication = db.Column(db.String(50), nullable=True)

    isDeleted = db.Column(db.Boolean)
    
    #Device mobile |or| web for jwt
    
    product = db.relationship('Product')
    
    
