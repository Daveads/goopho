from flask import request, jsonify, make_response, Blueprint
import uuid
from werkzeug.security import generate_password_hash, check_password_hash
from goopho.route import User
from goopho.route import db

#add flask_jwt
from flask_jwt_extended import create_access_token, set_access_cookies

signup = Blueprint('signup', __name__)



@signup.route('/signup', methods=['POST'])
def create_user():
    data = request.get_json()
    hashed_password = generate_password_hash(data['password'], method='sha256')
 
    new_user=User(public_id=str(uuid.uuid4()), name=data['name'], username=data['username'], email=data['email'], password=hashed_password, isDeleted=False)
    
    db.session.add(new_user)
    db.session.commit()
    
    user = User.query.filter_by(name=data['name']).first()

    access_token = create_access_token(identity=user.public_id)
    
    
    response = jsonify({"messge": "User created",
                            'email' : user.email,
                            'name' :  user.name,
                            'token' : access_token    
        })
    
    
    set_access_cookies(response, access_token)

    return response
