from flask import Blueprint, render_template, redirect, url_for
from flask_login import login_required, current_user
from ..models import Transactions
from .forms import TransactionForm
from ...app import api

transactions = Blueprint('transactions', __name__, template_folder="templates")

@transactions.route('/transactions', methods=["GET", "POST"])
@login_required
def get_transactions():
    transactions = []
    try:
        db_transactions = Transactions.objects.filter(userid=current_user.id)
        for transaction in db_transactions:
            transactions.append(transaction)
    except Transactions.DoesNotExist:
        transactions = None

    form = TransactionForm()

    return render_template('transactions.html', form=form, transactions=transactions)

@transactions.route('/transactions/dummy', methods=["GET"])
@login_required
def dummy():
    transaction = Transactions(userid=current_user.id, ordertype="order", volume=0.25, symbolIn="BTC", symbolOut="USD", prize=55619.16, costs=1390.47)
    transaction.save()
    return redirect(url_for('transactions.get_transactions'))
