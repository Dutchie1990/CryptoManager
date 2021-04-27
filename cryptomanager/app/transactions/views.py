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
    form.vs_currency.choices = get_currencies()

    if form.validate_on_submit():
        volume = form.volume.data
        coin_symbol = form.coin_symbol.data
        vs_currency = form.vs_currency.data
        prize = form.prize.data
        ordertype = form.ordertype.data
        usd_prize = float(form.usd_prize.data)

        assetOut = g.asset
        assetIn = coin_symbol if ordertype == "BUY" else vs_currency


        # update asset out
        assetOut_amount = assetOut.amount - prize if ordertype == "BUY" else assetOut.amount - volume
        if assetOut_amount > 0:
            Assets.objects(userid=assetOut.userid, asset_name=assetOut.asset_name).update_one(
                            set__amount=assetOut_amount)
        else:
            Assets.objects(userid=assetOut.userid,
                            asset_name=assetOut.asset_name).delete()
        
        #update or save assset in
        try:
            #asset exists
            assetIn_db = Assets.objects.get(
                    userid=assetOut.userid, asset_name=assetIn)
            assetIn_amount = assetIn_db.amount + volume if ordertype == "BUY" else assetIn_db.amount + prize
            if assetIn == "USD":
                Assets.objects(userid=assetOut.userid, asset_name=assetIn).update_one(
                        set__amount=assetIn_amount, upsert=False)
            else:
                costs = ((assetIn_db.costs * assetIn_db.amount) + (usd_prize * volume))/assetIn_amount
                Assets.objects(userid=assetOut.userid, asset_name=assetIn).update_one(
                        set__amount=assetIn_amount, set__costs=costs, upsert=False)

        except Assets.DoesNotExist:
            #asset doesnt exist
            if assetIn == "USD":
                new_asset = Assets(userid=assetOut.userid, asset_name=assetIn, amount=(volume if ordertype == "BUY" else prize))
            else:      
                new_asset = Assets(userid=assetOut.userid, asset_name=assetIn, amount=(volume if ordertype == "BUY" else prize), costs=usd_prize)
            new_asset.save()
        
        transaction = Transactions(userid=assetOut.userid, ordertype=ordertype.lower(), volume=volume,
                                       coin_symbol=coin_symbol, vs_currency=vs_currency, prize=(prize/volume), costs=prize)
        transaction.save()
        return redirect(url_for('transactions.get_transactions'))

    return render_template('add_transaction.html', form=form)


def get_currencies():
    exclude_fiat = ["aed", "ars", "aud", "bdt", "bmd",  "bhd", "brl", "cad", "chf", "clp", "cny", "czk", "dkk", "eur", "gbp", "hkd", "huf", "idr", "ils", "inr", "jpy",
                    "krw", "kwd", "lkr", "mmk", "mxn", "myr", "ngn", "nok", "nzd", "php", "pkr", "pln", "rub", "sar", "sek", "sgd", "thb", "try", "twd", "uah", "vef", "vnd", "zar"]
    return [y.upper() for y in api.supported_vs_currency if [x for x in api.supported_coins] and y not in exclude_fiat]
