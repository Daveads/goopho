from flask import Flask, jsonify
from flask_restful import Api
from flasgger import Swagger, swag_from

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

api = Api(app)


app.config['SWAGGER'] = {
    'title': 'Goopho route api doc',
    'uiversion': 2
}

swag = Swagger(app)

##
## ROUTES 
##

from goopho.routes.auth.logout import logOut

from goopho.routes.admin.Admin import Admin

from goopho.routes.user.checkstuff import checkdata
from goopho.routes.user.upload import upload
from goopho.routes.user.getupload import getUpload

# route blueprint register
app.register_blueprint(Admin)
app.register_blueprint(logOut)
app.register_blueprint(checkdata)
app.register_blueprint(upload)
app.register_blueprint(getUpload)



from goopho.routes.auth.signup import create_user
from goopho.routes.auth.login import login
###
# route resources
###
api.add_resource(create_user, "/signup")
api.add_resource(login, "/login")

#######################################################
# Todo 
# work on super root user.... 
# auto add a super user if it does'nt exist
#######################################################


#
# MODEL INSTANT FOR EXTERNAL USER
from goopho.models.users import User, setRole


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


@app.errorhandler(500)
def internal_error(error):

    return jsonify({'message': 'we will get back to you soon'}), 500
