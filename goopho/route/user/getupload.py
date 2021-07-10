from flask import request, jsonify, Blueprint
from flask_jwt_extended import jwt_required
from flask_jwt_extended import get_jwt_identity

import os
from goopho.route import app
from goopho.route import Product
from goopho.route import Image


getUpload = Blueprint('getUpload', __name__)


@getUpload.route('/getupload', methods=['GET'])
@jwt_required()
def uploadFiles():
    
    
    return jsonify ({})


  
