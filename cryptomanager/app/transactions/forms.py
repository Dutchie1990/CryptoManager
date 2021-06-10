from flask import flash, g
# Extension for implementing WTForms for managing web forms
from flask_wtf import FlaskForm
from wtforms.fields import FloatField, StringField, SelectField, HiddenField
from wtforms.validators import InputRequired, DataRequired, ValidationError
from ..models import Assets
from ...app import api


class TransactionForm(FlaskForm):
    """Class TransactionForm

    Attributes:
        volume:
        coin_symbol
        vs_currency
        prize
        ordertype
        usd_prize

    Methods:
        validate_volume:
            param: volume field
        Method to check if the user have sufficient funds
        to make the transaction
    """
    volume = FloatField(("Volume"), validators=[
                                        InputRequired("Input is required!"),
                                        DataRequired("Data is required!")
                                    ])
    coin_symbol = SelectField(("BUY / SELL"),
                              choices=[(x['symbol']).upper() for x
                                       in api.supported_coins],
                              validators=[
                                        InputRequired("Input is required!"),
                                        DataRequired("Data is required!")
                                    ])
    vs_currency = SelectField(("VS Currency"), choices=[], validators=[
                                        InputRequired("Input is required!"),
                                        DataRequired("Data is required!")
                                    ])
    prize = FloatField(("Prize"), validators=[
                                        InputRequired("Input is required!"),
                                        DataRequired("Data is required!")
                                    ])
    ordertype = SelectField(("Order Type"), choices=["BUY", "SELL"],
                            validators=[
                                        InputRequired("Input is required!"),
                                        DataRequired("Data is required!")
                                    ])
    usd_prize = HiddenField()

    @staticmethod
    def validate_volume(form, field):
        if form.ordertype.data == "BUY":
            try:
                asset = Assets.objects.get(userid=g.user.id,
                                           asset_name=form.vs_currency.data)
            except Assets.DoesNotExist:
                raise ValidationError('Insufficient funds to make the order')
            if form.prize.data > asset.amount:
                raise ValidationError('Insufficient funds to make the order')
            flash("You bought {} {} for {} {}".format(form.volume.data,
                                                      form.coin_symbol.data,
                                                      form.prize.data,
                                                      form.vs_currency.data),
                  "success")
        else:
            try:
                asset = Assets.objects.get(userid=g.user.id,
                                           asset_name=form.coin_symbol.data)
            except Assets.DoesNotExist:
                raise ValidationError('Insufficient funds to make the order')
            if field.data > asset.amount:
                raise ValidationError('Insufficient funds to make the order')
            flash("You sold {} {} for {} {}".format(form.volume.data,
                                                    form.coin_symbol.data,
                                                    form.prize.data,
                                                    form.vs_currency.data),
                  "success")
        g.asset = asset
