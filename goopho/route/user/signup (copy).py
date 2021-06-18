from flask import request, jsonify, make_response
from goopho.route import app
import uuid
from werkzeug.security import generate_password_hash, check_password_hash
from goopho.route import User
from goopho.route import db
import jwt
import datetime

@app.route('/signup', methods=['GET'])
def testing_user():
    me = "david"
    print(app)
    print(User)
    #return jsonify({'message' : "working"})
    return ("working " + me)


@app.route('/signup', methods=['POST'])
def create_user():
    data = request.get_json()
    hashed_password = generate_password_hash(data['password'], method='sha256')
 
    new_user=User(public_id=str(uuid.uuid4()), first_name=data['first_name'], last_name=data['last_name'], username=data['username'], admin=False, email=data['email'], password=hashed_password)
 
    db.session.commit()
        
    db.session.add(new_user)


    #meant to send token, username, email immidately after sign up
    """
    user = User.query.filter_by(name=data['username']).first()
    token = jwt.encode({'public_id' : user.public_id, 'exp' : datetime.datetime.utcnow() + datetime.timedelta(minutes=30)}, app.config['SECRET_KEY'], algorithm="HS256")



    return jsonify({'message' : 'New user created!',
                    'email'  : user.email,
                    'username' : user.username,
                    'token' : token
    })
    """

    return jsonify({'message' : "usercreated"})
 
    
