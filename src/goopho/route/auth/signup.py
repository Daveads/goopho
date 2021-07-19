from re import I
from flask import jsonify, make_response
from flask_restful import Resource, reqparse, abort
from flasgger import swag_from

import uuid
from werkzeug.security import generate_password_hash, check_password_hash

from goopho.route import User
from goopho.route import db


#add flask_jwt
from flask_jwt_extended import create_access_token, set_access_cookies, get_csrf_token

signup_args = reqparse.RequestParser()
signup_args.add_argument("name", type=str, help="Name fields is required", required=True)
signup_args.add_argument("password", type=str, help="password fields is required", required=True)
signup_args.add_argument("username", type=str, help="username fields is required", required=True)
signup_args.add_argument("email", type=str, help="email fields is required", required=True)


class create_user(Resource):

    @swag_from('/goopho/docs/signup_specs.yml', methods=['POST'])
    def post(self):

        data = signup_args.parse_args()
        ## email and username should be unique
        
        user_name = User.query.filter_by(username=data['username']).first()

        email = User.query.filter_by(email=data['email']).first()

        count = 0
        
        
        data_check = data.copy()
        
        for i in data_check :
            if data_check[i] == "" :

                abort(409, message=f"{i} can't be empty")


        if user_name:
            abort(409, message="user name already exist...")
	    
        if email and email.isDeleted == False :
            # this is still a test
            # if email already in database it either the user forgot he/her password or an intruder is trying to get in to the acc 
            # so a email should be send to the "user"
            abort(409, message="email already exist...")
	    
        hashed_password = generate_password_hash(data['password'], method='sha256')
 
        new_user=User(public_id=str(uuid.uuid4()), name=data['name'], username=data['username'], email=data['email'], password=hashed_password, isDeleted=False)
    
        db.session.add(new_user)

        db.session.commit()
    
        user = User.query.filter_by(name=data['name']).first()

        access_token = create_access_token(identity=user.public_id)
    
        csrf_token = get_csrf_token(access_token)
    
    
        response = jsonify({"messge": "User created",
                            'email' : user.email,
                            'name' :  user.name,
                            'username' : user.username,
                            'token' : access_token,
                            'csrf_token' : csrf_token  
        })
    
    
        set_access_cookies(response, access_token)

        return response
