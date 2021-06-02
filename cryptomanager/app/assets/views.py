from flask import Blueprint, render_template, flash, redirect, url_for, g
from flask_login import login_required, current_user
from .forms import DepositForm
from ..models import Assets, User, Transactions
from ...app import api
import copy
import json

assets = Blueprint('assets', __name__, template_folder="templates")


@assets.route('/assets', methods=["GET", "POST"])
@login_required
def get_asset():
    if not current_user:
        redirect(url_for('auth.login'))
        flash("You need to be logged in for this functionality", "error")
    g.user = current_user
    form = DepositForm()
    list_assets = []
    current_value = 0
    completed_assets_list = []
    withdrawable_balance = 0

    try:
        db_assets = Assets.objects.filter(userid=current_user.id)
        for asset in db_assets:
            list_assets.append(asset)
    except Assets.DoesNotExist:
        list_assets = None
    if list_assets:
        usd_balance = next(
            (x for x in list_assets if x.asset_name == "USD"), None)
        if usd_balance:
            withdrawable_balance = usd_balance.amount
            list_assets.remove(usd_balance)
        updated_list_assets = api.retrieve_current_prizes(
                                                        '/simple/price',
                                                        list_assets)
        completed_assets_list = Assets.calculate_profits(updated_list_assets)
        current_value = (Assets.calculate_current_value(completed_assets_list)
                         + withdrawable_balance)

    if form.validate_on_submit():
        transaction_type = form.transaction_type.data.lower()
        amount = form.amount.data
        if transaction_type == 'deposit':
            withdrawable_balance = g.value
        else:
            withdrawable_balance = g.value
        if withdrawable_balance == 0:
            Assets.objects(userid=g.user.id, asset_name='USD').delete()
        else:
            Assets.objects(userid=g.user.id, asset_name='USD').update_one(
                            set__amount=withdrawable_balance, upsert=True)
        transaction = Transactions(userid=g.user.id,
                                   ordertype=transaction_type, volume=amount)
        transaction.save()

    return render_template('assets.html', form=form,
                           assets=completed_assets_list,
                           withdrawable_balance=withdrawable_balance,
                           current_value=current_value)


@assets.route('/fetch_owned_assets', methods=["GET"])
@login_required
def fetch_owned_assets():
    try:
        db_assets = Assets.objects.filter(userid=current_user.id)
        return db_assets.to_json()
    except Assets.DoesNotExist:
        return None


@assets.route('/fetch_supported_assets', methods=["GET"])
@login_required
def fetch__supported_assets():
    return json.dumps(api.supported_coins)
