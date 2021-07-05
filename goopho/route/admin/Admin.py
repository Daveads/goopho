from flask import request, jsonify, make_response, Blueprint
from goopho.route import User
from flask_jwt_extended import jwt_required
from flask_jwt_extended import get_jwt_identity


Admin = Blueprint('admin', __name__)



#Admin test
@Admin.route('/admin', methods=['GET'])
@jwt_required()
def admin():
    
    current_user = get_jwt_identity()
    print()
    
    user = User.query.filter_by(public_id=current_user).first()
    
    cu = user
    
    if cu.roles == "Admin":
    
    	return jsonify({'message': 'Admin!!!!'})
    	
    else:
    	  return jsonify({'message': 'Not An Admin !'}), 401
    
    
