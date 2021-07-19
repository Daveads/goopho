from os import name
from re import I
from goopho.models import db
from sqlalchemy.sql import func
import enum 
from datetime import datetime 


from werkzeug.security import generate_password_hash
import uuid


datenow = datetime.now()

class setRole(enum.Enum):
    user = "User"
    admin = "Admin"
    special = "Special"


class User(db.Model):

    __tablename__ = "user"

    id = db.Column(db.Integer, primary_key=True)

    public_id = db.Column(db.String(50), unique=True)

    name = db.Column(db.String(50), nullable=False)

    username = db.Column(db.String(50), nullable=False)
    
    email = db.Column(db.String(50), nullable=False)

    password = db.Column(db.String(200), nullable=False)

    roles = db.Column(db.Enum(setRole), default=setRole.user)
    
    registered_on = db.Column(db.String(20), nullable=False)

    #stores time user update profile
    updated_at = db.Column(db.DateTime(timezone=True), nullable=True)
    
    email_verification = db.Column(db.DateTime, default=None, nullable=True)

    isDeleted = db.Column(db.Boolean, default=False)
    
    #Device mobile |or| web for jwt
    
    products = db.relationship('Product', backref='user')


    def __init__(self, name, username, email, password, roles=setRole.user):

        self.public_id = str(uuid.uuid4())
        self.name = name
        self.username = username
        self.email = email
        self.password =  generate_password_hash(password, method='sha256')
        self.roles = roles
        self.registered_on = datenow.strftime("%d/%m/%Y %H:%M:%S")
