from flask import request, jsonify, Blueprint

from flask_jwt_extended import jwt_required
from flask_jwt_extended import get_jwt_identity

from werkzeug.utils import secure_filename
import os

from goopho.route import app
from goopho.route import db
from goopho.route import Product
from goopho.route import Image

upload = Blueprint('upload', __name__)



def allowed_file(filename):

    return '.' in filename and filename.rsplit('.', 1)[1].lower() in app.config['ALLOWED_EXTENSIONS']


@upload.route('/upload', methods=['POST'])
@jwt_required()
def uploadFiles():
   
    if 'file' not in request.files:
        
        return jsonify ({'message' : "no file part in the request"})

    
    files = request.files.getlist('file')
    
    picname = []

    for file in files:

        

        if file.filename == '':
        
            
            return jsonfiy ({'message' : "file does not exist"})


        if file and allowed_file(file.filename):

            filename = secure_filename(file.filename)

            picname.append(file.filename)

            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            
            
        else:

            return jsonify({'message' : 'file type not allowed'})


    data = request.get_json()

    
    """
    product = Product(small_description=data['description'], long_description=['long description'], user_pub_id=get_jwt_identity())
    db.session.add(product)
    db.session.commit()
    
    
    product = Product.query.filter_by(name=data['name']).first()
    product_id = product.id
    
    for i in picname:
    
        image = Image(image_name=i, product_id=product_id)
        
        db.session.add(images)
        
    	db.session.commit()
    """
    
    print(picname)
    for i in picname:
        print(i)
        
    return jsonify({'message' : 'File(s) successfully uploaded'})    
