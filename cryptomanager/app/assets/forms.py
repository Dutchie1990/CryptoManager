from flask import g, flash
# Extension for implementing WTForms for managing web forms
from flask_wtf import FlaskForm
from wtforms.fields import FloatField, HiddenField
from wtforms.validators import InputRequired, DataRequired, ValidationError
from ..models import Assets


class DepositForm(FlaskForm):
    amount = FloatField(("Amount"),
                        validators=[
        InputRequired("Input is required!"),
        DataRequired("Data is required!")
    ])
    transaction_type = HiddenField()

    @staticmethod
    def validate_amount(form, field):
        try:
            available_asset = Assets.objects.get(userid=g.user.id, asset_name='USD')
        except Assets.DoesNotExist:
            if (form.transaction_type.data == 'Withdrawal'):
                flash("Insufficient funds to withdraw", "error")
                raise ValidationError()
            g.value = field.data
            return
        if (form.transaction_type.data == 'Withdrawal'):
            if field.data > available_asset.amount:
                flash("Insufficient funds to withdraw", "error")
                raise ValidationError()
            g.value = available_asset.amount - field.data
            return
        g.value = available_asset.amount + field.data
        return