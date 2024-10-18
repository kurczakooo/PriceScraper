import numpy as np
import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import threading
#import matplotlib.pyplot as plt
#import seaborn as sns
from urls import samsung_odyssey_g5_ceneo_url, xiaomi_g34wqi_ceneo_url
from ceneo.scrape_price import scrape_ceneo_price
from chromedriver_config.chromedriver_config import user_agent_string_override_command, chrome_options
from data_management import DataManager


#next I need to implement an algorithm to randomize the user string
PATH  = './chromedriver-win64/chromedriver.exe'
PATH_LINUX = '/usr/bin/chromedriver/chromedriver'

samsung_prices_file = "data/samsung_g5_price_history.csv"
xiaomi_prices_file = "data/xiaomi_g34wqi_price_history.csv"


def main_fuction(SYSTEM_PATH, chromedriver_options, user_agent_string_override, url, data_file_path, url_type=None):
    service = Service(SYSTEM_PATH)
    driver = webdriver.Chrome(service = service, options=chromedriver_options)
    # Sends a Chrome DevTools Protocol (CDP) command to override the user-agent string
    driver.execute_cdp_cmd('Network.setUserAgentOverride', {"userAgent": user_agent_string_override})

    driver.get(url)
    prices_list = scrape_ceneo_price(driver=driver)
    current_price = prices_list[0]

    dataManager = DataManager(data_file_path)
    dataManager.load_data()
    dataManager.add_row(current_price)
    dataManager.save_df_to_path()



if __name__ == "__main__":
    th1 = threading.Thread(
        target=main_fuction, 
        args=[PATH, chrome_options, user_agent_string_override_command, samsung_odyssey_g5_ceneo_url, samsung_prices_file])
    
    th2 = threading.Thread(
        target=main_fuction, 
        args=[PATH, chrome_options, user_agent_string_override_command, xiaomi_g34wqi_ceneo_url, xiaomi_prices_file])
    
    th1.start()
    th2.start()