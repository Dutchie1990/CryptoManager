import requests
import os


class API():
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

        supported_images = [''.join(val.split())[
                :-4] for val in os.listdir("cryptomanager/app/static/img/symbols")]

        for item in response.json():   
            if item['symbol'] in supported_images:
                cls.supported_coins.append({'symbol':item['symbol'], 'id':item['id'], 'name':item['name']})
    
    @classmethod
    def retrieve_vs_currencies(cls, rel_url):
        url = cls.BASE_URL + rel_url 

        response = requests.get(url)

        # Throw an exception on HTTP errors (404, 500, etc).
        response.raise_for_status()

        supported_images = [''.join(val.split())[
                :-4] for val in os.listdir("cryptomanager/app/static/img/symbols")]

        for item in response.json():   
            if item in supported_images:
                cls.supported_vs_currency.append(item)


    def retrieve_current_prize(self, rel_url, list_assets):
        url = self.BASE_URL + rel_url

        for asset in list_assets:
            for coin in self.supported_coins:
                if (asset.asset_name).lower() == coin['symbol']:
                    asset.id = coin['id']

        querystring = ""
        querystring = (','.join(x.id for x in list_assets)).lower()

        payload = {'ids': querystring, 'vs_currencies': "usd"}
        response = requests.get(url, payload)

        x = response.json()

        for asset in list_assets:
            asset.prize = x[asset.id]['usd']

        return list_assets
