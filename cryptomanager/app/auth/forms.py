# Extension for implementing WTForms for managing web forms
from flask_wtf import FlaskForm
from wtforms.fields import StringField, SubmitField, PasswordField
from wtforms.validators import InputRequired, DataRequired, Length, ValidationError, Email, EqualTo
#Import User class to validate if user exists
from ..models import User

class RegistrationForm(FlaskForm):
    firstname         = StringField(("Firstname *"),
                                validators=[
                                    InputRequired("Input is required!"),
                                    DataRequired("Data is required!"),
                                    Length(min=5, max=20, message="Firstname must be between 5 and 20 characters long")
                                ])
    email            = StringField(("Email *"),
                                validators=[
                                    InputRequired("Input is required!"),
                                    DataRequired("Data is required!"),
                                    Length(min=5, max=30, message="Email must be between 5 and 30 characters long"),
                                    Email("You did not enter a valid email!")
                                ])
    password         = PasswordField(("password *"),
                                validators=[
                                    InputRequired("Input is required!"),
                                    DataRequired("Data is required!"),
                                    Length(min=5, max=40, message="Password must be between 10 and 40 characters long"),
                                    EqualTo("password_confirm", message="Passwords must match")
                                ])
    password_confirm = PasswordField(("Confirm Password *"),
                                validators=[
                                    InputRequired("Input is required!"),
                                    DataRequired("Data is required!")
                                ])
    submit           = SubmitField(("Register"))

    def validate_email(self, form, field):
        user = User.objects(email=field.data)
        if user:
            raise ValidationError("Email already exists.")
