from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
app.config.from_object("config.Test_db_with_sqlite")
db = SQLAlchemy(app)
migrate = Migrate(app, db)

#routes 
from goopho.route.user import signup
from goopho.route.admin import admin



