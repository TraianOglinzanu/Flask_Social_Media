import os
from flask import Flask 
from flask_sqlalchemy import SQLAlchemy 
from flask_migrate import Migrate
from flask_login import LoginManager

app = Flask(__name__)

### Setting up database ###

basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URAI'] = 'sqlite:///'+os.path.join(basedir, 'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = get_flashed_messages()

db = SQLAlchemy(app)
Migrate(app)

### Setting up login configuration ###

login_manager = LoginManager()

login_manager.init_app(app)
login_manager.login_view = 'users.login'

from hockeyblog.core.views import core
from hockeyblog.users.views import users
from hockeyblog.error_pages.handlers import error_pages

app.register_blueprint(core)
app.register_blueprint(users)
app.register_blueprint(error_pages)





