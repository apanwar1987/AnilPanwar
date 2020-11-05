# import libraries
import requests
from Comman import commonBase
import json

def get_weather_data_from_api():
    # het url from config
    URL = commonBase.read_json_config()['API']

    # hit get api to get response
    response = requests.get(url=URL)
    response = response.json()

    # dump response in json file
    with open('./OutPut/API_Out.json', 'w+', encoding='utf-8') as file:
        json.dump(response, file)
