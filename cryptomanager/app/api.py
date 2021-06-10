import requests
import os


class API():
    """ API class

    Attributes:
        :BASE_URL: The base url of the API
        :supported_coins: The crypto's which are supported by the application
        :supported_vs_currency: The currencies which can be used
                                to trade against
    Methods:
        retrieve_symbols:
            param: rel_url
        Method to get all the coins supported by the API

        retrieve_vs_currencies:
            param: rel_url
        Method to get all the VS currencies supported by the API

        retrieve_current_prizes:
            param: rel_url, list_assets
        Method to get the current prices of the list of assets

        retrieve_current_prize:
            param: rel_url, asset
        Method to get the current price of one asset

    """
    BASE_URL = 'http://api.coingecko.com/api/v3'
    supported_coins = []
    supported_vs_currency = []

    def __init__(self, *args, **kwargs):
        super(API, self).__init__(*args, **kwargs)

    @classmethod
    def retrieve_symbols(cls, rel_url):
        url = cls.BASE_URL + rel_url

        response = requests.get(url)

        # Throw an exception on HTTP errors (404, 500, etc).
        response.raise_for_status()

        # Filter based on the images supported by the application
        supported_images = [''.join(val.split())[
                :-4] for val in
                os.listdir("cryptomanager/app/static/img/symbols")]

        # get only 1 id for 1 symbol
        uniqueSymbol = []
        for item in response.json():
            if(item["symbol"] not in uniqueSymbol):
                uniqueSymbol.append(item["symbol"])
                if item['symbol'] in supported_images:
                    cls.supported_coins.append(
                        {'symbol': item['symbol'],
                            'id': item['id'], 'name': item['name']})

    @classmethod
    def retrieve_vs_currencies(cls, rel_url):
        url = cls.BASE_URL + rel_url

        response = requests.get(url)

        # Throw an exception on HTTP errors (404, 500, etc).
        response.raise_for_status()

        supported_images = [''.join(val.split())[
                :-4] for val in
                    os.listdir("cryptomanager/app/static/img/symbols")]

        # Filter based on the images supported by the application

        for item in response.json():
            if item in supported_images:
                cls.supported_vs_currency.append(item)

    def retrieve_current_prizes(self, rel_url, list_assets):
        for asset in list_assets:
            for coin in self.supported_coins:
                if (asset.asset_name).lower() == coin['symbol']:
                    asset.id = coin['id']

        querystring = ""
        querystring = (','.join(x.id for x in list_assets)).lower()

        x = self.retrieve_current_prize(rel_url, querystring)

        for asset in list_assets:
            asset.prize = x[asset.id]['usd']

        return list_assets

    def retrieve_current_prize(self, rel_url, querystring):
        url = self.BASE_URL + rel_url
        payload = {'ids': querystring, 'vs_currencies': "usd"}
        return requests.get(url, payload).json()
