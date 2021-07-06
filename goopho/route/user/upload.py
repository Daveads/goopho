from flask import request, jsonify, Blueprint
from flask_jwt_extended import jwt_required
from goopho.route import app
from werkzeug.utils import secure_filename
import os

upload = Blueprint('upload', __name__)



def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in app.config['ALLOWED_EXTENSIONS']
    
    retu
           

@upload.route('/upload', methods=['POST'])
#@jwt_required()
def uploadFiles():
    
    if 'file' not in request.files:
        
        return jsonify ({'message' : "no file part in the request"})
        
    
    file = request.files['file']
    
    if file.filename == '':
    
        return jsonfiy ({'message' : "file does not exist"})
        
    
    if file and allowed_file(file.filename):

        
        filename = secure_filename(file.filename)
        
        print(filename)

        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))

 	    

        return jsonify({'message' : 'File(s) successfully uploaded'})
 
 
    else:
        return jsonify({'message' : 'file type not allowed'}) 









"""
def allowed_file(filename):
    
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


    

@upload.route('/upload', methods=['POST'])
#@jwt_required()
def uploadFiles():

    files= request.files
    
    print(files)
    
    print(request.files)
    if 'files[]' not in request.files:
    	resp = jsonify({'message' : "no file part in the request"})
    	resp.status_code = 400
    	
    	return resp
    
    errors = {}
    
    success = False
    
    
    for file in files:
    
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            
            success = True
            
            
        else: 
             errors[file.filename] = 'file type is not allowed'
             
     
     
     
     
    if success and errors:
    	 
    	 errors['message'] = 'File(s) successfully uploaded'
    	 resp = jsonify(errors)
    	 
    	 resp.status_code = 500
    	 return resp
    	 
    	 
    	 
    else:
    	  resp = jsonify(errors)
    	  resp.status_code = 500
    	  
    	  return resp     
"""   	  
    	  



"""
@upload.route('/upload', methods=['POST'])
def uploadFiles():


    file = request.files['inputFile']
    
    filename = secure_filename(file.filename)
    
    file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
    
    errors['message'] = 'File(s) successfully uploaded'
    
    resp = jsonify(errors)
    	 
    return resp
"""
