from flask import request, jsonify, make_response
from goopho.route import app
import uuid
from werkzeug.security import generate_password_hash, check_password_hash
from goopho.route import User
from goopho.route import db
import jwt
import datetime

@app.route('/signup', methods=['POST'])
def create_user():
    data = request.get_json()
    hashed_password = generate_password_hash(data['password'], method='sha256')
 
    new_user=User(public_id=str(uuid.uuid4()), name=data['username'], email=data['email'], password=hashed_password, admin=False)
    
    db.session.add(new_user)
    db.session.commit()
    
    user = User.query.filter_by(username=data['username']).first()

    token = jwt.encode({'public_id' : user.public_id, 'exp' : datetime.datetime.utcnow() + datetime.timedelta(minutes=30)}, app.config['SECRET_KEY'], algorithm="HS256")
    
    
    return jsonify({
                    'email'  : user.email,
                    'username' : user.username,
                    'token' : token
                    })
    

 
    
