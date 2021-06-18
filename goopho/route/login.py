from flask import request, jsonify, make_response
from goopho.route import app
from goopho.route import User
from werkzeug.security import check_password_hash
import jwt
import datetime
from functools import wraps

def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = None
        
        if 'x-access-token' in request.headers:
            token = request.headers['x-access-token']
            
        if not token:
            return jsonify({'message' : 'Token is missing'})


        try:
            data = jwt.decode(token, app.config['SECRET_KEY'], algorithms="HS256")
            current_user = User.query.filter_by(public_id=data['public_id']).first()
        
        except:
            return jsonify({'message': 'Token is invalid!'}), 401
        
        return f(current_user, *args, **kwargs)

    return decorated



@app.route('/login')
def login():
    auth = request.authorization
    
    if not auth or not auth.username or not auth.password:
    
       return make_response("could not authenticat", 401, {'WWW-Authenticate': 'Basic realm="Login required!"'})
       
    user = User.query.filter_by(name=auth.username).first()
       
       
    if not user:
        return make_response("could not authenticat", 401, {'WWW-Authenticate': 'Basic realm="Login required!"'})
        
        
        
    if check_password_hash(user.password, auth.password):

        token = jwt.encode({'public_id' : user.public_id, 'exp' : datetime.datetime.utcnow() + datetime.timedelta(minutes=30)}, app.config['SECRET_KEY'], algorithm="HS256")

        cod = token

        return jsonify({'token' : cod })


    
    return  make_response("could not authenticat", 401, {'WWW-Authenticate': 'Basic realm="Login required!"'})


    
