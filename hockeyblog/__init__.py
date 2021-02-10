import os
from flask import Flask 
from flask_sqlalchemy import SQLAlchemy 
from flask_migrate import Migrate
from flask_login import LoginManager

app = Flask(__name__)

### Setting up Database ###

basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URAI'] = 'sqlite:///'+os.path.join(basedir, 'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = get_flashed_messages()

db = SQLAlchemy(app)
Migrate(app)

from hockeyblog.core.views import core
from hockeyblog.error_pages.handlers import error_pages

app.register_blueprint(core)
app.register_blueprint(error_pages)