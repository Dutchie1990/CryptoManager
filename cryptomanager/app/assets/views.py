from flask import Blueprint, render_template, flash, redirect, url_for
from flask_login import login_required, current_user
from .forms import DepositForm
from ..models import Assets, User
from ...app import api

assets = Blueprint('assets', __name__, template_folder="templates")


@assets.route('/assets', methods=["GET", "POST"])
def get_asset():
    form = DepositForm()

    try:
        assets = Assets.objects.filter(userid=current_user.id)
    except Assets.DoesNotExist:
        assets = None 

    return render_template('assets.html', form=form, assets=assets)

@assets.route('/deposit', methods=["POST", "GET"])
@login_required
def deposit_asset():
    asset = Assets(current_user.id, "USD", 10000.00)
    asset.save()
    return render_template('assets.html',)

