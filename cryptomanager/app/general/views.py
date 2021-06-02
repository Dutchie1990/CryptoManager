from flask import Blueprint, render_template
from flask_login import current_user, login_required, login_user, logout_user
from ...app import app, db
from ..models import User

general = Blueprint("general", __name__)


@general.route("/")
@general.route("/home")
def home():
    return render_template("welcomescreen.html")
