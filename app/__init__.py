from flask import Flask
import os
from flask_jwt_extended import JWTManager
from datetime import timedelta

app = Flask(__name__)
app.secret_key = os.environ.get("APP_SECRET_KEY")

app.config["JWT_SECRET_KEY"] = os.environ.get("APP_SECRET_KEY")
app.config['JWT_TOKEN_LOCATION'] = ['cookies']
app.config['JWT_COOKIE_CSRF_PROTECT'] = False
app.config["JWT_ACCESS_TOKEN_EXPIRES"] = timedelta(minutes=20)
jwt = JWTManager(app)

from app.controllers import user,pokemon