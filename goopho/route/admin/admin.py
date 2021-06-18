from flask import request, jsonify, make_response
from goopho.route import app
import uuid
from werkzeug.security import generate_password_hash, check_password_hash
from goopho.route import User


@app.route('/admin', methods=['GET'])
def testing_admin():
    me = "david"
    print(app)
    print(User)
    #return jsonify({'message' : "working"})
    return ("Admin " + me)




