# Imports from FLASK
from flask import g, flash
# Extension for implementing WTForms for managing web forms
from flask_wtf import FlaskForm
# Import fields from WTForms
from wtforms.fields import FloatField, HiddenField
# Import validators from WTForms
from wtforms.validators import InputRequired, DataRequired, ValidationError
# Import database model
from ..models import Assets


class DepositForm(FlaskForm):
    """Class DepositForm

    Attributes:
        amount: The amount which the user want to deposit or withdrawal

    Methods:
        validate_amount:
            param: amount field
        Method to check whether the user have sufficient amount to withdrawal
    """

    amount = FloatField(("Amount"),
                        validators=[
        InputRequired("Input is required!"),
        DataRequired("Data is required!")
    ])
    transaction_type = HiddenField()

    @staticmethod
    def validate_amount(form, field):
        try:
            available_asset = Assets.objects.get(userid=g.user.id,
                                                 asset_name='USD')
        except Assets.DoesNotExist:
            if (form.transaction_type.data == 'withdrawal'):
                flash("Insufficient funds to withdraw", "error")
                raise ValidationError()
            g.value = field.data
            flash("{} is added to your deposit".format(field.data), "success")
            return
        if (form.transaction_type.data == 'withdrawal'):
            if field.data > available_asset.amount:
                flash("Insufficient funds to withdraw", "error")
                raise ValidationError()
            g.value = available_asset.amount - field.data
            flash("{} is withdrawn from your deposit".format(field.data),
                  "success")
            return
        g.value = available_asset.amount + field.data
        flash("{} is added to your deposit".format(field.data), "success")
        return
