from flask import Flask
from flask_restful import Api
from src.config import Config
from flask_sqlalchemy import SQLAlchemy
from werkzeug.exceptions import default_exceptions
from flask_cors import CORS

from flask_migrate import Migrate

app = Flask(__name__)
api = Api(app)
cors = CORS()


app.config['SQLALCHEMY_DATABASE_URI'] = Config.SQLALCHEMY_DATABASE_URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = Config.SQLALCHEMY_TRACK_MODIFICATIONS
app.config['SQLALCHEMY_ECHO'] = True
app.config['BUNDLE_ERRORS'] = Config.BUNDLE_ERRORS

db = SQLAlchemy(app)
migrate = Migrate(app, db)
cors.init_app(app=app)

api.prefix = Config.API_PREFIX

from src.routes import set_routes

set_routes(api)

from src.error import handle_error

for ex in default_exceptions:
    app.register_error_handler(ex, handle_error)
