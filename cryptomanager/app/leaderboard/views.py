from flask import Blueprint, render_template
from ..models import Assets, User
from ...app import api

leaderboard = Blueprint('leaderboard', __name__, template_folder='templates')

@leaderboard.route('/leaderboard')
def get_leaderboard():
    users = User.objects().only('id', 'firstname').to_json()
    assets_names= [x.lower() for x in Assets.objects().distinct(field="asset_name") if x != "USD"]
    getid = lambda assets : [x['id'] for x in api.supported_coins if x['symbol'] in assets]
    assets_querystring = ",".join(getid(assets_names))
    prices = api.retrieve_current_prize('/simple/price', assets_querystring)
    print(users)
    print(prices)
    return render_template('leaderboard.html')
