import requests
import os

class API():
    BASE_URL = 'http://api.coingecko.com/api/v3'
    supported_coins = []

    def __init__(self):
        pass

    @classmethod
    def retrieve_symbols(cls, rel_url):
        url = cls.BASE_URL + rel_url

        response = requests.get(url)
 
        # Throw an exception on HTTP errors (404, 500, etc).
        response.raise_for_status()

        for item in response.json():
            supported_images = [''.join(val.split())[:-4] for val in os.listdir("cryptomanager/app/static/img/symbols")]
            if item['symbol'] in supported_images:
                cls.supported_coins.append(item)
