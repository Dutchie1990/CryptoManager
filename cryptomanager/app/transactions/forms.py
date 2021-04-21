from flask import flash
# Extension for implementing WTForms for managing web forms
from flask_wtf import FlaskForm
from wtforms.fields import FloatField, StringField,SelectField
from wtforms.validators import InputRequired, DataRequired, ValidationError
from ..models import Assets
from ...app import api

class TransactionForm(FlaskForm):
    volume = FloatField(("Volume"), validators=[
                                        InputRequired("Input is required!"),
                                        DataRequired("Data is required!")
                                    ])
    symbolIn = SelectField(("Buy"), choices= [(x['symbol']).upper() for x in api.supported_coins], validators=[
                                        InputRequired("Input is required!"),
                                        DataRequired("Data is required!")
                                    ])
    symbolOut = SelectField(("Sell"), choices= [], validators=[
                                        InputRequired("Input is required!"),
                                        DataRequired("Data is required!")
                                    ])
    prize = StringField(("Prize"), validators=[
                                        InputRequired("Input is required!"),
                                        DataRequired("Data is required!")
                                    ])
