from flask import request, jsonify, make_response

from flask_restful import Resource, abort
from flasgger import swag_from



from goopho.routes import User
from werkzeug.security import check_password_hash

#add flask_jwt
from flask_jwt_extended import create_access_token, set_access_cookies, get_csrf_token

class login(Resource):
    
    def get(self):
        
        auth = request.authorization


        if not auth or not auth.username or not auth.password:
            
            return make_response("could not authenticat", 401, {'WWW-Authenticate': 'Basic realm="Login required!"'})
       
        
        user = User.query.filter_by(username=auth.username).first()
    
      
        if not user:
         return make_response("could not authenticate", 401, {'WWW-Authenticate': 'Basic realm="Login required!"'})
        
        
        
        if check_password_hash(user.password, auth.password):
            
            access_token = create_access_token(identity=user.public_id)
            csrf_token = get_csrf_token(access_token)
        
            response = jsonify({
                            'token' : access_token,
                            'csrf_token' : csrf_token,
                            'email_verfication' : user.email_verification,
                            'delete_status' : user.isDeleted
                            })
	    
            set_access_cookies(response, access_token)
	
            return response

 
        return  make_response("could not authenticate", 401, {'WWW-Authenticate': 'Basic realm="Login required!"'})
