# importing libraries
from selenium import webdriver
import chromedriver_autoinstaller
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from Comman import commonBase
import time
import json

# list/dict to adds weather info
weather_info = []
dict_weather = {}
keys = []
values = []

# explicit wait time
wait_time = int(commonBase.read_json_config()['wait'])

def get_weather_details_fromUI():
    # initialize chrome instance and open ndtv url
    chromedriver_autoinstaller.install()
    driver = webdriver.Chrome()
    driver.get(commonBase.read_json_config()['URL'])
    driver.maximize_window()


    # wait for "No Thanks" element to load
    element = WebDriverWait(driver, wait_time).until(
            EC.presence_of_element_located((By.CLASS_NAME, commonBase.read_json_locators()['No_Thanks'])))
    element.click()
    # click on '...' sub menu
    element = WebDriverWait(driver, wait_time).until(
        EC.presence_of_element_located((By.ID, commonBase.read_json_locators()['Sub_Menu'])))
    element.click()

    # click on Weather link
    element = WebDriverWait(driver, wait_time).until(
        EC.presence_of_element_located((By.XPATH, commonBase.read_json_locators()['Weather_link'])))
    element.click()

    # wait for map page to load
    element = WebDriverWait(driver, wait_time).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, commonBase.read_json_locators()['Wait_for_map'])))

    # unselect all checkboxes
    checkboxes = WebDriverWait(driver, wait_time).until(EC.presence_of_all_elements_located
                                                      ((By.CSS_SELECTOR, commonBase.read_json_locators()['checkboxes_for_unselect'])))

    time.sleep(2)
    for each_checkbox in checkboxes:
            if each_checkbox.is_selected(): # just to be sure that you make check, but not uncheck
                driver.execute_script('arguments[0].click()', each_checkbox)

    # send value in pin textbox like "Dehradun'
    element = WebDriverWait(driver, wait_time).until(
        EC.presence_of_element_located((By.CLASS_NAME, commonBase.read_json_locators()['Search_textBox'])))
    element.send_keys(commonBase.read_json_config()['City'])
    element.click()

    # Select city checkbox
    element = WebDriverWait(driver, wait_time).until(
        EC.presence_of_element_located((By.ID, commonBase.read_json_config()['City'])))
    element.click()

    # click on city from Map using title
    element = WebDriverWait(driver, wait_time).until(
        EC.presence_of_element_located((By.XPATH, '//*[@title="%s"]' % commonBase.read_json_config()['City'])))
    element.click()

    # get weather info from pop up

    weather_details = WebDriverWait(driver, wait_time).until(EC.presence_of_all_elements_located
                                                      ((By.XPATH, commonBase.read_json_locators()['weather_info'])))


    for weather in weather_details:
        weather = str(weather.text)
        weather_info.append(weather)

    while "" in weather_info:
        weather_info.remove("")

    for info in weather_info:
        info = str(info).split(":")
        keys.append(info[0])
        values.append(info[1])

    ndtv_result = dict(zip(keys, values))

    with open('./OutPut/ndtv_out.json', 'w+') as file:
        json.dump(ndtv_result, file)


    #quit browser
    driver.quit()


