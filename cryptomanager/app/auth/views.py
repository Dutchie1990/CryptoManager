# Imports from Flask
from flask import Blueprint, render_template, flash, abort, url_for, redirect
# Extension for implementing Flask-Login for authentication
from flask_login import current_user, login_required, login_user, logout_user
# Imports from the app package
from ...app import app, db
from ..models import User

from .forms import RegistrationForm, LoginForm, ManageForm, DeleteForm

auth = Blueprint("auth", __name__, template_folder="templates")


@auth.route("/register", methods=["GET", "POST"])
def register():
    if current_user.is_authenticated:
        return redirect(url_for("general.home"))

    form = RegistrationForm()

    if form.validate_on_submit():
        firstname = form.firstname.data
        email = form.email.data.lower()
        password = form.password.data
        user = User(firstname, email, password)
        user.set_password(password)
        user.save()
        flash(("You are registered"), "success")
        login_user(user)
        return redirect(url_for('assets.get_asset'))

    return render_template('register.html', form=form)


@auth.route('/login', methods=["GET", "POST"])
def login():
    if current_user.is_authenticated:
        return redirect(url_for("general.home"))

    form = LoginForm()

    if form.validate_on_submit():
        user = User.objects.filter(email=form.email.data.lower()).first()
        if user is None or not user.check_password(form.password.data):
            flash("Invalid username or password", "error")
            return redirect(url_for('auth.login'))
        login_user(user)
        flash(("You are logged in"), "success")
        return redirect(url_for('assets.get_asset'))

    return render_template("login.html", form=form)


@auth.route("/logout")
@login_required
def logout():
    logout_user()
    flash("You have been logged out", "error")
    return redirect(url_for("general.home"))


@auth.route("/manage", methods=["GET", "POST"])
@login_required
def manage():
    user_email = {'email': current_user.email}
    form_update = ManageForm(data=user_email)
    form_delete = DeleteForm()

    if form_update.new_password.data and form_update.validate_on_submit():
        user = User.objects.filter(
                                email=form_update.email.data.lower()).first()
        if user is None or not user.check_password(
                                            form_update.old_password.data):
            flash("Your old password is not correct", "error")
            return redirect(url_for('auth.manage'))
        hashed_password = user.set_password(form_update.new_password.data)
        user.save()
        flash("Your succesfully changed your password", "success")
    if form_delete.validate_on_submit():
        user = User.objects.filter(
                                email=current_user.email).first()
        if user is None or not user.check_password(
                                            form_delete.delete_password.data):
            flash("Your old password is not correct", "error")
            return redirect(url_for('auth.manage'))
        user.delete()
        flash("Your succesfully deleted your account", "success")
        return redirect(url_for('general.home'))
    return render_template("manage.html",
                           form_update=form_update,
                           form_delete=form_delete)
