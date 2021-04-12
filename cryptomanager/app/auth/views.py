# Imports from Flask
from flask import render_template, flash, abort, url_for, redirect
# Extension for implementing Flask-Login for authentication
from flask_login import current_user, login_required, login_user, logout_user
#Imports from the app package 
from ...app import app, db
from ..models import User

from .forms import RegistrationForm, LoginForm

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
        return redirect(url_for('home'))

    return render_template('register.html', form=form)

@app.route('/login', methods=["GET", "POST"])
def login():
    if current_user.is_authenticated:
        return redirect(url_for("home"))
    
    form = LoginForm()

    if form.validate_on_submit():
        user = User.objects.filter(email=form.email.data).first()
        if user is None or not user.check_password(form.password.data):
            flash("Invalid username or password")
            return redirect(url_for('login'))
        login_user(user)
        return redirect(url_for('home'))

    return render_template("login.html", form=form)

@app.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for("home"))