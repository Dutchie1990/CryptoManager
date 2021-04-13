from flask import Blueprint, render_template, flash, redirect, url_for
from flask_login import login_required, current_user
from .forms import DepositForm
from ..models import Assets, User
from ...app import api
import copy

assets = Blueprint('assets', __name__, template_folder="templates")


@assets.route('/assets', methods=["GET", "POST"])
def get_asset():
    form = DepositForm()
    list_assets = []

    try:
        db_assets = Assets.objects.filter(userid=current_user.id)
        for asset in db_assets:
            list_assets.append(asset)
    except Assets.DoesNotExist:
        list_assets = None
    if list_assets:
        withdrawable_balance = next(
            (x for x in list_assets if x.asset_name == "USD"), None)
        if withdrawable_balance:
            list_assets.remove(withdrawable_balance)
    updated_list_assets = api.retrieve_current_prize(
        '/simple/price', list_assets)
    completed_assets_list = Assets.calculate_profits(updated_list_assets)
    current_value = Assets.calculate_current_value(completed_assets_list)
    return render_template('assets.html', form=form, assets=completed_assets_list, withdrawable_balance=withdrawable_balance, current_value=current_value)


@assets.route('/deposit', methods=["POST", "GET"])
@login_required
def deposit_asset():
    asset = Assets(current_user.id, "USD", 10000.00, 10000.00)
    asset.save()
    asset = Assets(current_user.id, "BTC", 1.00, 50000.00)
    asset.save()
    asset = Assets(current_user.id, "DOT", 450.00, 7.80)
    asset.save()
    asset = Assets(current_user.id, "ETH", 20.5, 1500.26)
    asset.save()
    return render_template('assets.html',)
