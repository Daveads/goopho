import re
from flask import request, jsonify, make_response, Blueprint

from flask_restful import Resource, reqparse, abort
from flasgger import swag_from



from goopho.route import User
from werkzeug.security import check_password_hash

#add flask_jwt
from flask_jwt_extended import create_access_token, set_access_cookies, get_csrf_token

"""
login_auth = reqparse.RequestParser()
login_auth.add_argument("username", type=str, help="username required for login", required=True)
login_auth.add_argument("password", type=str, help="password required for login", required=True)
"""

class login(Resource):
    
    def get(self):
        
        auth = request.authorization


        if not auth or not auth.username or not auth.password:
            
            return make_response("could not authenticat", 401, {'WWW-Authenticate': 'Basic realm="Login required!"'})
       
        
        user = User.query.filter_by(username=auth.username).first()
    
        #just testing out something
        user_data={}
    
        user_data['public_id']= user.public_id
    
        user_data['role']= user.roles
    
        user_data['email_verif']= user.email_verfication
    
        user_data['acct_creation'] = user.acct_create_at
    
        #print(user_data)
       
        if not user:
         return make_response("could not authenticate", 401, {'WWW-Authenticate': 'Basic realm="Login required!"'})
        
        
        
        if check_password_hash(user.password, auth.password):
            
            access_token = create_access_token(identity=user.public_id)
            csrf_token = get_csrf_token(access_token)
        
            response = jsonify({
                            'token' : access_token,
                            'csrf_token' : csrf_token
                            })
	    
            set_access_cookies(response, access_token)
	
	  
            """return jsonify({'token' : access_token,
        		'message': "login successful"
                })"""
     
	    
            return response

 
        return  make_response("could not authenticate", 401, {'WWW-Authenticate': 'Basic realm="Login required!"'})



