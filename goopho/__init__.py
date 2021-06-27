from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_cors import CORS

app = Flask(__name__)
app.config.from_object("config.DevelopmentConfig")
db = SQLAlchemy(app)
cors = CORS(app, resorces={r'/*': {"origins": '*'}})

migrate = Migrate(app, db)

#routes 
from goopho.route.user import signup
from goopho.route.admin import admin



