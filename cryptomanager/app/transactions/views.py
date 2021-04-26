from flask import Blueprint, render_template, redirect, url_for, flash, g
from flask_login import login_required, current_user
from ..models import Transactions, Assets
from .forms import TransactionForm
from ...app import api


transactions = Blueprint('transactions', __name__, template_folder="templates")

@transactions.route('/transactions', methods=["GET", "POST"])
@login_required
def get_transactions():
    if not current_user:
        redirect(url_for('auth.login'))
        flash("You need to be logged in for this functionality", "error")
    transactions = []

    try:
        db_transactions = Transactions.objects.filter(userid=current_user.id)
        for transaction in db_transactions:
            transactions.append(transaction)
    except Transactions.DoesNotExist:
        transactions = None

    return render_template('transactions.html', transactions=transactions)

@transactions.route('/add_transaction', methods=["GET", "POST"])
@login_required
def add_transaction():
    if not current_user:
        redirect(url_for('auth.login'))
        flash("You need to be logged in for this functionality", "error")
    g.user = current_user
    form = TransactionForm()
    form.symbolOut.choices = get_currencies()

    if form.validate_on_submit():
        volume = form.volume.data
        symbolIn = form.symbolIn.data
        symbolOut = form.symbolOut.data
        prize = form.prize.data
        ordertype = form.ordertype.data
        usd_prize = float(form.usd_prize.data)

        if ordertype == "BUY":
            #save the asset out to the database
            assetOut = g.asset
            amount = assetOut.amount - prize
            #if amount is 0, delete otherwise update
            if amount > 0:
                Assets.objects(userid=assetOut.userid, asset_name=assetOut.asset_name).update_one(set__amount=amount)
            else:
                Assets.objects(userid=assetOut.userid, asset_name=assetOut.asset_name).delete()
            #check if new asset exists
            try:
                asset = Assets.objects.get(userid=assetOut.userid, asset_name=symbolIn)
                amount = asset.amount + volume
                costs = ((asset.costs * asset.amount) + (volume * usd_prize))/amount
                Assets.objects(userid=assetOut.userid, asset_name=symbolIn).update_one(set__amount=amount, set__costs=costs, upsert=False)
            except Assets.DoesNotExist:
                new_asset = Assets(userid=assetOut.userid, asset_name=symbolIn, amount=volume, costs=usd_prize)
                new_asset.save()
            transaction = Transactions(userid=assetOut.userid, ordertype=ordertype,volume=volume, symbolIn=symbolIn,symbolOut=symbolOut,prize=(prize/volume),costs=prize)
            transaction.save()

    return render_template('add_transaction.html', form=form)


@transactions.route('/transactions/dummy', methods=["GET"])
@login_required
def dummy():
    transaction = Transactions(userid=current_user.id, ordertype="order", volume=0.25, symbolIn="BTC", symbolOut="USD", prize=55619.16, costs=1390.47)
    transaction.save()
    return redirect(url_for('transactions.get_transactions'))

def get_currencies():
        list_assets = []
        try:
            db_assets = Assets.objects.filter(userid= current_user.id)
            for asset in db_assets:
                list_assets.append(asset)
            return [x.asset_name.upper() for x in list_assets if x.asset_name.lower() in [y for y in api.supported_vs_currency]]
        except Assets.DoesNotExist:
            return None