# Imports from Flask
from flask import render_template, flash, abort, url_for, redirect
# Extension for implementing Flask-Login for authentication
from flask_login import current_user, login_required, login_user, logout_user
#Imports from the app package 
from ...app import app, db
from ..models import User

from .forms import RegistrationForm

@app.route("/register", methods=["GET", "POST"])
def register():
    if current_user.is_authenticated:
        return redirect(url_for("home"))
    
    form = RegistrationForm()
    
    if form.validate_on_submit():
        firstname        = form.firstname.data
        email            = form.email.data
        password         = form.password.data
        user = User(firstname, email, password)
        user.set_password(password)
        user.save()
        flash(("You are registered."), "success")
        login_user(user)

    return render_template('register.html', form=form)
