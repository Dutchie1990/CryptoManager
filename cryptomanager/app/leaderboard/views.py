from flask import Blueprint, render_template

leaderboard = Blueprint('leaderboard', __name__, template_folder='templates')

@leaderboard.route('/leaderboard')
def get_leaderboard():
    return render_template('leaderboard.html')