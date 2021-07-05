from flask import request, jsonify, make_response
from goopho.route import app
from goopho.route import User
from werkzeug.security import check_password_hash
import jwt
import datetime


@app.route('/login')
def login():

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
    
    print(user_data)
       
    if not user:
        return make_response("could not authenticate", 401, {'WWW-Authenticate': 'Basic realm="Login required!"'})
        
        
        
    if check_password_hash(user.password, auth.password):

        token = jwt.encode({'public_id' : user.public_id, 'exp' : datetime.datetime.utcnow() + datetime.timedelta(minutes=30)}, app.config['SECRET_KEY'], algorithm="HS256")

        cod = token

        return jsonify({'token' : cod })


    
    return  make_response("could not authenticate", 401, {'WWW-Authenticate': 'Basic realm="Login required!"'})


