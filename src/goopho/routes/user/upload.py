from flask import jsonify, request

from flask_restful import Resource, abort

from flask_jwt_extended import jwt_required
from flask_jwt_extended import get_jwt_identity

from werkzeug.utils import secure_filename

from goopho.routes import db
from goopho.routes import Product
from goopho.routes import Image
from goopho.routes import User
from goopho.routes import app

import os
import uuid


def allowed_file(filename):

    return '.' in filename and filename.rsplit('.', 1)[1].lower() in app.config['ALLOWED_EXTENSIONS']


class upload(Resource):

    @jwt_required()
    def post(self):
        
        
        if 'file' not in request.files:
            
            return jsonify ({'message' : "no file part in the request"})

    
        files = request.files.getlist('file')
        data = request.values.copy()
    

        picname = []

    
        for file in files:
            
            
            if file.filename == '':
                
                return jsonify ({'message' : "file does not exist"})


            if file and allowed_file(file.filename):
                
                filename = secure_filename(file.filename)
                
                picname.append(file.filename)
                
                file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            
            
            else:
                
                return jsonify({'message' : 'file type not allowed'})



        user = User.query.filter_by(public_id=get_jwt_identity()).first()

        if user :
            
            #assign a product_id 
            product_pub_id = str(uuid.uuid4())
            product = Product(title=data['title'], description=data['description'], user_pub_id=user.id, product_pub_id=product_pub_id)
            db.session.add(product)
            db.session.commit()

        else:

            abort(409, message=" an error occured in the database")
    
        product = Product.query.filter_by(product_pub_id=product_pub_id).first()
        product_id = product.id
    
        for i in picname:
          image = Image(image=i, product_id=product_id)
          db.session.add(image)

        db.session.commit()
    
     
        return jsonify({'message' : 'File(s) successfully uploaded'})
