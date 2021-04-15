from flask import Blueprint, render_template, flash, redirect, url_for, g
from flask_login import login_required, current_user
from .forms import DepositForm
from ..models import Assets, User
from ...app import api
import copy

assets = Blueprint('assets', __name__, template_folder="templates")


@assets.route('/assets', methods=["GET", "POST"])
@login_required
def get_asset():
    if not current_user:
        redirect(url_for('auth.login'))
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
        updated_list_assets = api.retrieve_current_prize(
        '/simple/price', list_assets)
        completed_assets_list = Assets.calculate_profits(updated_list_assets)
        current_value = Assets.calculate_current_value(completed_assets_list) + withdrawable_balance
    
    if form.validate_on_submit():
        transaction_type = form.transaction_type.data
        if transaction_type == 'Deposit':
            withdrawable_balance = g.value
        else:
            withdrawable_balance = g.value
        if withdrawable_balance == 0:
            Assets.objects(userid=g.user.id, asset_name='USD').delete()
        else:
            Assets.objects(userid=g.user.id, asset_name='USD').update_one(set__amount=withdrawable_balance, upsert=True)

    return render_template('assets.html', form=form, assets=completed_assets_list, withdrawable_balance=withdrawable_balance, current_value=current_value)

