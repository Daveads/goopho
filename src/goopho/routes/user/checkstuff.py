from flask import request, jsonify, Blueprint
from goopho.routes import User
from flask_jwt_extended import jwt_required
from flask_jwt_extended import get_jwt_identity

checkdata = Blueprint('check', __name__)


#testing out token required

@checkdata.route('/checkdata', methods=['GET'])
@jwt_required()
def datacheck():

    print(get_jwt_identity())
    
    return  jsonify({'message': 'working'})
   
 

