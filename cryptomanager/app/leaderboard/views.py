# Import functionalities from FLASK
from flask import Blueprint, render_template
# Import functionalities from FLASK login
from flask_login import current_user
# Import datebase models
from ..models import Assets, User
# Import api to make api calls
from ...app import api

leaderboard = Blueprint('leaderboard', __name__, template_folder='templates')


@leaderboard.route('/leaderboard')
def get_leaderboard():
    user = None
    if current_user:
        this_user = current_user
    leaderboard_data = []

    # Get all users
    users = User.objects().only('id', 'firstname')
    # Get all assets owned by all users distinct
    assets_names = [x.lower() for x in Assets.objects().distinct(
                                field="asset_name") if x != "USD"]
    assets_querystring = ",".join(getid_list(assets_names))
    # Get the current prices
    prices = api.retrieve_current_prize('/simple/price', assets_querystring)

    for user in users:
        usd_balance = 0
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
            asset.prize = (prices["".join(get_id(asset.asset_name.lower()))]
                           ['usd'])
        updated_list_assets = Assets.calculate_profits(list_assets)
        user_info = LeaderboardUser(user=user, assets=updated_list_assets,
                                    usd_balance=usd_balance)
        # Get the percentage of the asset
        user_info.calculate_assets_percentage()
        # Calculate total profit of user
        user_info.calculate_total_profit()
        # Append to leaderboard data
        leaderboard_data.append(user_info)
    leaderboard_data.sort(key=sort_criteria, reverse=True)

    return render_template('leaderboard.html',
                           leaderboard_data=leaderboard_data[:10],
                           user=this_user,
                           counter=0)


class LeaderboardUser:
    """ API class

    Methods:
        def calculate_assets_percentage:
            param: none
        Method to calculate how much of the portfolio is a specific
        asset in percentage

        calculate_total_profit:
            param: none
        Method to calculate total profit per user
    """
    def __init__(self, user, assets, usd_balance):
        self.user = user
        self.assets = assets
        self.usd_balance = usd_balance

    def calculate_assets_percentage(self):
        total_value = (sum([(x.prize * x.amount) for x in self.assets])
                       + self.usd_balance.amount
                       if self.usd_balance
                       else sum([(x.prize * x.amount) for x in self.assets]))
        if self.usd_balance:
            self.usd_balance.percentage = (self.usd_balance.amount /
                                           total_value) * 100
        for asset in self.assets:
            asset.percentage = ((asset.prize * asset.amount) /
                                total_value) * 100

    def calculate_total_profit(self):
        self.user.total_profit = sum([x.p_l for x in self.assets])


def sort_criteria(e):
    """
        param: leaderboard data
        Helper to get the sorting key
    """
    return e.user.total_profit


def getid_list(assets):
    """
        param: list of asset
        Helper to get the id of the coin in order to call the API
    """
    return [x['id'] for x in api.supported_coins if x['symbol'] in assets]


def get_id(assets):
    """
        param: asset
        Helper to get the id of the coin in order to get specific
        data from API response
    """
    return [x['id'] for x in api.supported_coins if x['symbol'] == assets]
