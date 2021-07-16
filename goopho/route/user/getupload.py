from flask import request, jsonify, Blueprint, send_from_directory, current_app, send_file
from flask_jwt_extended import jwt_required
from flask_jwt_extended import get_jwt_identity

import os
from goopho.route import app
from goopho.route import Product
from goopho.route import Image


getUpload = Blueprint('getUpload', __name__)


@getUpload.route('/getupload', methods=['GET'])
#@jwt_required()
def uploadFiles():
    
    name = "1.png"
    
    #return jsonify ({'message' : "fuck you"})
    
    
    #return send_from_directory(directory=app.config["UPLOAD_FOLDER"], filename=name, as_attachment=True)


    #download image from a flask rest api
    
    #print(app.config["UPLOAD_FOLDER"] + name)
    
    uploads = os.path.join(app.root_path, app.config['UPLOAD_FOLDER'])
    
    up= app.config['UPLOAD_FOLDER']
    print(up)
    
    
    #print(app.static_folder)
    
    #return send_file(app.config["UPLOAD_FOLDER"] + f"/{name}")
    
    #goopho/goopho/uploads/1.png
    
    
    
    #works don't know why
    #return send_file("uploads/Screenshot_from_2020-07-09_09-52-12.png", as_attachment=True)
    
    return  send_from_directory(directory="uploads/", path=name, mimetype='image/png', as_attachment=True)

