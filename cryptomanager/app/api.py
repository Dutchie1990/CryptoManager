import requests
import os

class API():
    
    @staticmethod
    def retrieve_data(rel_url):
        BASE_URL = 'http://api.coingecko.com/api/v3'
        supported_coins = []
        url = BASE_URL + rel_url
        response = requests.get(url)
 
        # Throw an exception on HTTP errors (404, 500, etc).
        response.raise_for_status()
 
        # Parse the response as JSON and return a Python dict.
        for item in response.json():
            supported_images = [''.join(val.split())[:-4] for val in os.listdir("cryptomanager/app/static/img/symbols")]
            if item['symbol'] in supported_images:
                supported_coins.append(item)
        return supported_coins
