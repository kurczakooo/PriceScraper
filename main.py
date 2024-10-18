import numpy as np
import pandas as pd
#import requests
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
#from selenium.webdriver.chrome.options import Options
#from selenium.webdriver.common.by import By
#from selenium.webdriver.support.ui import WebDriverWait
#from selenium.webdriver.support import expected_conditions as EC
import time
from datetime import datetime
#import matplotlib.pyplot as plt
#import seaborn as sns
#from bs4 import BeautifulSoup
from urls import samsung_odyssey_g5_ceneo_url, xiaomi_g34wqi_ceneo_url
from ceneo.scrape_price import scrape_ceneo_price
from chromedriver_config.chromedriver_config import user_agent_string_override_command, chrome_options

price_df = pd.DataFrame(columns=['price', 'time'])

#next I need to implement an algorithm to randomize the user string
PATH  = './chromedriver-win64/chromedriver.exe'
PATH_LINUX = '/usr/bin/chromedriver/chromedriver'



samsung_prices_file = "data/samsung_g5_price_history.csv"
xiaomi_prices_file = "data/xiaomi_g34wqi_price_history.csv"


service = Service(PATH)
driver = webdriver.Chrome(service = service, options=chrome_options)
# Sends a Chrome DevTools Protocol (CDP) command to override the user-agent string
driver.execute_cdp_cmd('Network.setUserAgentOverride', {"userAgent": user_agent_string_override_command})


driver.get(xiaomi_g34wqi_ceneo_url)
samsung_odyssey_g5_ceneo_prices = scrape_ceneo_price(driver=driver)



df = pd.read_csv(samsung_prices_file, header=0, index_col=0)
df['data'] = pd.to_datetime(df['data'])




current_price = samsung_odyssey_g5_ceneo_prices[0]
formatted_time = pd.to_datetime(datetime.now())

print(f'\n cena: {current_price}, data: {formatted_time}')

df.loc[len(df)] = [current_price, formatted_time]
    
df.to_csv(samsung_prices_file)    
print('\ndodano wiersz do historii')
