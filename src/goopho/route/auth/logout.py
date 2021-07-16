from flask import Blueprint, jsonify
from flask_jwt_extended import unset_jwt_cookies


logOut = Blueprint('logout', __name__)

@logOut.route('/logout', methods=['POST'])
def logout():
    response = jsonify({"msg": "logout successful"})
    unset_jwt_cookies(response)
    
    return response



@logOut.route('/me', methods=['GET'])
def me():
    
    return '<h1>That me</h2>'
    
    
@logOut.route('/fuck', methods=['GET'])
def fuck():
    
    return 'Do you want to fuck'
