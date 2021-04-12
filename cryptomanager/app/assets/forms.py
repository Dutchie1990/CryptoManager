# Extension for implementing WTForms for managing web forms
from flask_wtf import FlaskForm
from wtforms.fields import SubmitField, FloatField
from wtforms.validators import InputRequired, DataRequired, Length, ValidationError, Email, EqualTo

class DepositForm(FlaskForm):
    deposit_amount =  FloatField(("Amount"),
                                validators=[
                                    InputRequired("Input is required!"),
                                    DataRequired("Data is required!")
                                ])
