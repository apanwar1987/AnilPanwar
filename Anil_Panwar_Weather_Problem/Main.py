from Weather_Info_UI_API import api, ndtv, comparator

if __name__ == "__main__":
    try:
        ndtv.get_weather_details_fromUI()
        api.get_weather_data_from_api()
        comparator.temprature_comparator()
    except Exception as error:
        print(error)
