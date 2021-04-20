from flask import Blueprint, render_template
from flask_login import login_required, current_user
from ..models import Transactions
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

    return render_template('transactions.html', transactions=transactions)
