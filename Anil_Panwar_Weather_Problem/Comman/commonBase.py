# import libraries
import json

def read_json_config():
    with open(r'./Config/config.json', 'r+') as file:
        data = json.load(file)
    return data

def read_json_locators():
    with open(r'./Config/locators.json', 'r+') as file:
        data = json.load(file)
    return data

