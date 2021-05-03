from flask import Blueprint, render_template
from ..models import Assets, User
from ...app import api

leaderboard = Blueprint('leaderboard', __name__, template_folder='templates')

@leaderboard.route('/leaderboard')
def get_leaderboard():
    leaderboard_data = []
    users = User.objects().only('id', 'firstname')
    assets_names= [x.lower() for x in Assets.objects().distinct(field="asset_name") if x != "USD"]
    getid = lambda assets : [x['id'] for x in api.supported_coins if x['symbol'] in assets]
    assets_querystring = ",".join(getid(assets_names))
    prices = api.retrieve_current_prize('/simple/price', assets_querystring)
    for user in users:
        list_assets = []
        updated_list_assets = []
        try:
            db_assets = Assets.objects.filter(userid=user.id)
            for asset in db_assets:
                list_assets.append(asset)
        except Assets.DoesNotExist:
            list_assets = None
        if list_assets:
            usd_balance = next(
                (x for x in list_assets if x.asset_name == "USD"), None)
        if usd_balance:
            list_assets.remove(usd_balance)
        for asset in list_assets:
            asset.prize = prices["".join(getid(asset.asset_name.lower()))]['usd']
        updated_list_assets = Assets.calculate_profits(list_assets)
        user_info = LeaderboardUser(user=user, assets=updated_list_assets, usd_balance=usd_balance)
        user_info.calculate_assets_percentage()
        user_info.calculate_total_profit()
        leaderboard_data.append(user_info)
    leaderboard_data.sort(key=sort_criteria)

        
    print(users)
    print(leaderboard_data)
    return render_template('leaderboard.html', leaderboard_data=leaderboard_data)

class LeaderboardUser:
    def __init__(self, user, assets, usd_balance):
        self.user = user
        self.assets = assets
        self.usd_balance = usd_balance
    
    def calculate_assets_percentage(self):
        total_value = sum([(x.prize) for x in self.assets]) + self.usd_balance.amount if self.usd_balance else sum([(x.prize) for x in self.assets]) 
        if self.usd_balance:
            self.usd_balance.percentage = (self.usd_balance.amount / total_value) * 100
        for asset in self.assets:
            asset.percentage = (asset.prize / total_value) * 100
    
    def calculate_total_profit(self):
        self.user.total_profit = sum([x.p_l for x in self.assets])

def sort_criteria(e):
    return e.user.total_profit