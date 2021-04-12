from flask import render_template
from flask_login import current_user, login_required, login_user, logout_user
#Imports from the app package 
from ...app import app, db
from ..models import User

@app.route("/")
@app.route("/home")
def home():
    return render_template("welcomescreen.html")

@app.template_filter("capitalized")
def capitalize(value):
    return value.capitalize()