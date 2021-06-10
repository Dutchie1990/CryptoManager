# Extension for implementing WTForms for managing web forms
from flask_wtf import FlaskForm
# Import functionalities from WTForms
from wtforms.fields import StringField, SubmitField, PasswordField
from wtforms.validators import (InputRequired, DataRequired,
                                Length, ValidationError, Email, EqualTo)
# Import database model
from ..models import User


class RegistrationForm(FlaskForm):
    """Class RegistrationForm

    Attributes:
        firstname: User's firstname
        email: User's email
        password: User's password
        password_confirm: Check to confirm password

    Methods:
        validate_email:
            param: email field
        Method to check if the user already exist in the database
    """

    firstname = StringField(("Firstname"),
                            validators=[
                                InputRequired("Input is required!"),
                                DataRequired("Data is required!"),
                                Length(min=2, max=20,
                                       message='''Firstname must be between 2
                                                and 20 characters long''')
                                ])
    email = StringField(("Email"),
                        validators=[
                                InputRequired("Input is required!"),
                                DataRequired("Data is required!"),
                                Length(min=5, max=30,
                                       message='''Email must be between 5
                                                and 30 characters long'''),
                                Email("You did not enter a valid email!")
                                ])
    password = PasswordField(("Password"),
                             validators=[
                                InputRequired("Input is required!"),
                                DataRequired("Data is required!"),
                                Length(min=5, max=40,
                                       message='''Password must be between 10
                                                and 40 characters long'''),
                                EqualTo("password_confirm",
                                        message="Passwords must match")
                                ])
    password_confirm = PasswordField(("Confirm Password"),
                                     validators=[
                                    InputRequired("Input is required!"),
                                    DataRequired("Data is required!")
                                ])

    @staticmethod
    def validate_email(form, field):
        user = User.objects(email=field.data.lower())
        if user:
            raise ValidationError("Email already exists.")


class LoginForm(FlaskForm):
    """Class LoginForm

    Attributes:
        email: User's email
        password: User's password
    """

    email = StringField(("Email"),
                        validators=[
                                    InputRequired("Input is required!"),
                                    DataRequired("Data is required!"),
                                    Length(min=5, max=30,
                                           message='''Email must be between 5
                                                    and 30 characters long'''),
                                    Email("You did not enter a valid email!")
                                ])
    password = PasswordField(("Password"),
                             validators=[
                                    InputRequired("Input is required!"),
                                    DataRequired("Data is required!"),
                                    Length(min=5, max=40,
                                           message='''Password must
                                                be between 10 and 40
                                                characters long'''),
                                ])


class ManageForm(FlaskForm):
    """Class ManageForm

    Attributes:
        email: User's email
        old_password: User's old password
        new_password: User's new password

    Methods:
        validate_old_password:
            param: old password field
        Method to check if the user chose another password
    """

    email = StringField(("Email"),
                        validators=[
                                Length(min=5, max=30,
                                       message='''Email must be between 5
                                                and 30 characters long'''),
                                Email("You did not enter a valid email!")
                                ])
    old_password = PasswordField(("Old password"),
                                 validators=[
                                Length(min=5, max=40,
                                       message='''Password must be between 10
                                                and 40 characters long'''),
                                ])
    new_password = PasswordField(("New password"),
                                 validators=[
                                Length(min=5, max=40,
                                       message='''Password must be between 10
                                                and 40 characters long'''),
                                ])

    @staticmethod
    def validate_old_password(form, field):
        if field.data == form.new_password.data:
            raise ValidationError('Please choose another password')


class DeleteForm(FlaskForm):
    """Class LoginForm

    Attributes:
        delete_password: User must enter correct password
        in order to delete account
    """
    delete_password = PasswordField(("Confirm password"),
                                    validators=[
                                    Length(min=5, max=40,
                                           message='''Password must be
                                                     between 10 and
                                                     40 characters long''')]
                                    )
