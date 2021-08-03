from flask import request, jsonify, make_response

from flask_restful import Resource, abort

from goopho.routes import User
from werkzeug.security import check_password_hash

#add flask_jwt
from flask_jwt_extended import (create_access_token, create_refresh_token)

class login(Resource):
    
    def post(self):
        
        auth = request.authorization


        if not auth or not auth.username or not auth.password:
            
            return make_response("could not authenticate", 401, {'WWW-Authenticate': 'Basic realm="Login required!"'})
       
        
        user = User.query.filter_by(username=auth.username).first()
    
      
        if not user:
         return make_response("could not authenticate", 401, {'WWW-Authenticate': 'Basic realm="Login required!"'})
        
        
        
        if check_password_hash(user.password, auth.password):
            
            identity = user.public_id

            print(identity)
            
            access_token = create_access_token(identity=identity)
            
            refresh_token = create_refresh_token(identity=identity)

        
            return jsonify({
                            'access_token' : access_token,
                            'refresh_token' : refresh_token,
                            'email_verfication' : user.email_verification,
                            'delete_status' : user.isDeleted,
                            'email' : user.email,
                            'username' : user.username
                            })
	    
        return  make_response("could not authenticate", 401, {'WWW-Authenticate': 'Basic realm="Login required!"'})
