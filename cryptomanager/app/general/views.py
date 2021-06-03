from flask import Blueprint, render_template, url_for, redirect
from flask_login import current_user, login_required, login_user, logout_user
from ...app import app, db
from ..models import User

general = Blueprint("general", __name__)


@general.route("/")
@general.route("/home")
def home():
    if current_user.is_authenticated:
        return redirect(url_for('assets.get_asset'))
    return render_template("welcomescreen.html")
