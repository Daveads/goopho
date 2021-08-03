from flask import Flask, jsonify
from flask_restful import Api

from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

from flask_cors import CORS


from flask_jwt_extended import JWTManager
    


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

##
## ROUTES  //remove
##

from goopho.routes.auth.logout import logOut

from goopho.routes.admin.Admin import Admin

from goopho.routes.user.checkstuff import checkdata
from goopho.routes.user.getupload import getUpload

# route blueprint register //remove this
app.register_blueprint(Admin)
app.register_blueprint(logOut)
app.register_blueprint(checkdata)
app.register_blueprint(getUpload)



from goopho.routes.auth.signup import create_user
from goopho.routes.auth.login import login
from goopho.routes.user.upload import upload
from goopho.routes.user.profile import profile
from goopho.routes.auth.refresh_token import RefreshToken


###
# route resources
###
api.add_resource(create_user, "/signup")
api.add_resource(login, "/login")
api.add_resource(upload, "/upload")
api.add_resource(profile, "/profile")
api.add_resource(RefreshToken, "/refreshtoken")


#
# MODEL INSTANT FOR EXTERNAL USER
from goopho.models.users import User, setRole
from goopho.models.products import Product
from goopho.models.images import Image


##
## create root on startup 
##

user = None
def create_root():
    
    try:
        global user        
        user = User.query.filter_by(username="goopho").first()

    except:
        print("                    * Database error table does not exist yet")


    if not user:
        
        try:
            
            datenow = datetime.now()
            
            date = datenow.strftime("%d/%m/%Y %H:%M:%S")
        
            new_user = User(name="Goopho", username="goopho", email="the.goopho@gmail.com", password="123456", roles=setRole.admin, email_verification=date)

            db.session.add(new_user)

            db.session.commit()

        
            print(" * Root user created !!!!")
            print(" * Email : the.goopho@gmail.com")
            print(" * Password : 123456")

        except:
            print("                    * Database error ('can not create root user' !!!!) ")

            return False

        return True

    else:
        return False

create_root()

"""
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
"""


@app.errorhandler(404)
def not_found(error):
	return jsonify({'message': 'Resource not found'}), 404


@app.errorhandler(500)
def internal_error(error):

    return jsonify({'message': 'we will get back to you soon'}), 500
