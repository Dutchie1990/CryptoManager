from flask import flash, g
# Extension for implementing WTForms for managing web forms
from flask_wtf import FlaskForm
from wtforms.fields import FloatField, StringField, SelectField, HiddenField
from wtforms.validators import InputRequired, DataRequired, ValidationError
from ..models import Assets
from ...app import api

class TransactionForm(FlaskForm):
    volume = FloatField(("Volume"), validators=[
                                        InputRequired("Input is required!"),
                                        DataRequired("Data is required!")
                                    ])
    symbolIn = SelectField(("BUY / SELL"), choices= [(x['symbol']).upper() for x in api.supported_coins], validators=[
                                        InputRequired("Input is required!"),
                                        DataRequired("Data is required!")
                                    ])
    symbolOut = SelectField(("VS Currency"), choices= [], validators=[
                                        InputRequired("Input is required!"),
                                        DataRequired("Data is required!")
                                    ])
    prize = FloatField(("Prize"), validators=[
                                        InputRequired("Input is required!"),
                                        DataRequired("Data is required!")
                                    ])
    ordertype = SelectField(("Ordertype"), choices=["BUY", "SELL"], validators=[
                                        InputRequired("Input is required!"),
                                        DataRequired("Data is required!")
                                    ])
    usd_prize = HiddenField()

    @staticmethod
    def validate_volume(form, field):
        if form.ordertype.data == "BUY":
            try:
                asset = Assets.objects.get(userid=g.user.id, asset_name=form.symbolOut.data)
            except Assets.DoesNotExist:
                raise ValidationError('Insufficient funds to make the order')
            if form.prize.data > asset.amount:
                raise ValidationError('Insufficient funds to make the order')
            flash("You bought {} {} for {} {}".format(form.volume.data, form.symbolIn.data, form.prize.data, form.symbolOut.data), "success")
        else:
            try:
                asset = Assets.objects.get(userid=g.user.id, asset_name=form.symbolIn.data)
            except Assets.DoesNotExist:
                raise ValidationError('Insufficient funds to make the order')
            if field.data > asset.amount:
                raise ValidationError('Insufficient funds to make the order')
            flash("You sold {} {} for {} {}".format(form.volume.data, form.symbolIn.data, form.prize.data, form.symbolOut.data), "success")
