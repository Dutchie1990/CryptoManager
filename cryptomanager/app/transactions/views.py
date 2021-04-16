from flask import Blueprint, render_template
from flask_login import login_required, current_user
from ..models import Assets, User
from ...app import api

transactions = Blueprint('transactions', __name__, template_folder="templates")

@transactions.route('/transactions', methods=["GET", "POST"])
@login_required
def get_transactions():
    return render_template('transactions.html')