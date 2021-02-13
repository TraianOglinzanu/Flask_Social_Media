from flask import render_template, url_for, flash, redirect, request, Blueprint
from flask_login import login_user, current_user, logout_user, login_required
from hockeyblog import db
from hockeyblog.models import User, BlogPost
from hockeyblog.users.forms import RegistrationForm, LoginForm, UpdateUserForm
from hockeyblog.users.picture_handler import add_profile_pic

users = Blueprint('users',__name__)










