from flask import Blueprint, render_template, flash, redirect, url_for
from flask_login import login_required, current_user
from .forms import DepositForm
from ..models import Assets, User

assets = Blueprint('assets', __name__, template_folder="templates")


@assets.route('/assets', methods=["GET", "POST"])
def get_asset():
    print(current_user)
    form = DepositForm()
    #try:
        #assets = Assets.objects.filter(userid=current_user.id)
    #except Assets.DoesNotExist:
        #assets = None 
    #print(assets)
    return render_template('assets.html', form=form)

@assets.route('/deposit', methods=["POST", "GET"])
def deposit_asset():
    asset = Assets(current_user.id, "USD", 10000.00)
    asset.save()
    return render_template('assets.html',)

