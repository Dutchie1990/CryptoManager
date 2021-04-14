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

    return render_template('assets.html', form=form, assets=completed_assets_list, withdrawable_balance=withdrawable_balance, current_value=current_value)


@assets.route('/deposit', methods=["POST", "GET"])
@login_required
def deposit_asset():
    asset = Assets(current_user.id, "USD", 10000.00, 10000.00)
    asset.save()
    asset = Assets(current_user.id, "BTC", 0.5, 50000.00)
    asset.save()
    asset = Assets(current_user.id, "DOT", 450.00, 7.80)
    asset.save()
    asset = Assets(current_user.id, "AE", 6.3, 1500.26)
    asset.save()
    asset = Assets(current_user.id, "ATOM", 6.3, 1500.26)
    asset.save()
    asset = Assets(current_user.id, "BNT", 6.3, 1500.26)
    asset.save()
    asset = Assets(current_user.id, "CNY", 6.3, 1500.26)
    asset.save()
    asset = Assets(current_user.id, "DAI", 6.3, 1500.26)
    asset.save()
    asset = Assets(current_user.id, "DASH", 6.3, 1500.26)
    asset.save()
    asset = Assets(current_user.id, "GUP", 6.3, 1500.26)
    asset.save()
    asset = Assets(current_user.id, "ION", 6.3, 1500.26)
    asset.save()
    asset = Assets(current_user.id, "LEO", 6.3, 1500.26)
    asset.save()
    asset = Assets(current_user.id, "OAX", 6.3, 1500.26)
    asset.save()
    asset = Assets(current_user.id, "PRL", 6.3, 1500.26)
    asset.save()
    asset = Assets(current_user.id, "SNT", 6.3, 1500.26)
    asset.save()
    asset = Assets(current_user.id, "UBQ", 6.3, 1500.26)
    asset.save()
    asset = Assets(current_user.id, "XAS", 6.3, 1500.26)
    asset.save()
    return render_template('assets.html',)
