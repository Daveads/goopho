from flask import request, jsonify
from flask_restful import Resource, abort

from flask_jwt_extended import jwt_required
from flask_jwt_extended import get_jwt_identity

from goopho.routes import User
from goopho.routes import Product
from goopho.routes import Image



class profile(Resource):
    
    pass;