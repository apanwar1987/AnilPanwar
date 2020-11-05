# import libraries
import json
from Comman import commonBase


def temprature_comparator():
    # read api data
    with open('./OutPut/API_Out.json', 'r+') as api:
        api_data = json.load(api)

    # read Ui weather data
    with open('./OutPut/ndtv_out.json', 'r+') as ndtv:
        ndtv_data = json.load(ndtv)

    # difference of temp from UI and API
    Diff_UI_API_Temp = (int(api_data['main']['temp']) - ((int(ndtv_data['Temp in Degrees']) * 1.8)+32))
    ## TESTS ##
    if Diff_UI_API_Temp > commonBase.read_json_config()['Temp_Min'] and Diff_UI_API_Temp < commonBase.read_json_config()['Temp_Max']:
        print("Diff_UI_API_Temp: ",Diff_UI_API_Temp)
        print("Temp_from_Api: ", api_data['main']['temp'])
        print("Temp_from_UI: ",ndtv_data['Temp in Degrees'] )
        print("Temp_Min: ", commonBase.read_json_config()['Temp_Min'])
        print("Temp_Max: ", commonBase.read_json_config()['Temp_Max'])
    else:
        print("Out OF Value")



