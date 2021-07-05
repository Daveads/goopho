from flask import request, jsonify, Blueprint
from goopho.route import User
from flask_jwt_extended import jwt_required

checkdata = Blueprint('check', __name__)



#testing out token required

@checkdata.route('/checkdata', methods=['GET'])
@jwt_required()
def datacheck():

    return  jsonify({'message': 'working'})
   
 

