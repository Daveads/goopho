from flask import Blueprint, jsonify
from flask_jwt_extended import unset_jwt_cookies


logO = Blueprint('logout', __name__)

@logO.route('/logout', methods=['POST'])
def logout():
    response = jsonify({"msg": "logout successful"})
    unset_jwt_cookies(response)
    return response



@logO.route('/me', methods=['GET'])
def me():
    
    return '<h1>That me</h2>'
    
    
@logO.route('/fuck', methods=['GET'])
def fuck():
    
    return 'Do you want to fuck'
