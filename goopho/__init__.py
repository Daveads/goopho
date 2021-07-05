from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_cors import CORS


from flask_jwt_extended import JWTManager
from flask_jwt_extended import create_access_token
from flask_jwt_extended import get_jwt
from flask_jwt_extended import get_jwt_identity
from flask_jwt_extended import jwt_required
from flask_jwt_extended import JWTManager
from flask_jwt_extended import set_access_cookies
from flask_jwt_extended import unset_jwt_cookies


from datetime import datetime
from datetime import timezone
from datetime import timedelta


# APP INSTANTS
app = Flask(__name__)
app.config.from_object("config.Test_db_with_sqlite")
db = SQLAlchemy(app)
cors = CORS(app, resorces={r'/*': {"origins": '*'}})
jwt = JWTManager(app)
migrate = Migrate(app, db)


##
## ROUTES
##
from goopho.route.auth.logout import logO
from goopho.route.auth.signup import signup
from goopho.route.auth.login import logIn
from goopho.route.admin.Admin import Admin
from goopho.route.user.checkstuff import checkdata


app.register_blueprint(Admin)
app.register_blueprint(logO)
app.register_blueprint(checkdata)
app.register_blueprint(logIn)
app.register_blueprint(signup)




@app.after_request
def refresh_expiring_jwts(response):
    try:
        exp_timestamp = get_jwt()["exp"]
        now = datetime.now(timezone.utc)
        target_timestamp = datetime.timestamp(now + timedelta(minutes=30))
        if target_timestamp > exp_timestamp:
            access_token = create_access_token(identity=get_jwt_identity())
            set_access_cookies(response, access_token)
        return response
    except (RuntimeError, KeyError):
        # Case where there is not a valid JWT. Just return the original respone
        return response
        
        
@app.errorhandler(404)
def not_found(error):
	return jsonify({'message': 'Resource not found'}), 404
