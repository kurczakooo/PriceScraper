import numpy as np
import pandas as pd
#import requests
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from datetime import datetime
#import matplotlib.pyplot as plt
#import seaborn as sns
from bs4 import BeautifulSoup
from urls import samsung_odyssey_g5_ceneo_url
from ceneo.scrape_price import scrape_ceneo_price

price_df = pd.DataFrame(columns=['price', 'time'])

#next I need to implement an algorithm to randomize the user string
PATH  = './chromedriver-win64/chromedriver.exe'
PATH_LINUX = '/usr/bin/chromedriver/chromedriver'

user_agent_string = "user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.37 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
user_agent_string_override_command = user_agent_string.split('=')[1]

chrome_options = Options()
# Headless mode
chrome_options.add_argument("--headless")
# Disable a feature which may tell the browser that it's being controlled by automation software
chrome_options.add_argument("--disable-blink-features=AutomationControlled")
# Disable sandbox for headless mode
chrome_options.add_argument("--no-sandbox")
# Disable gpu acceleration, since we're using headless mode
chrome_options.add_argument("--disable-gpu")
# Disable webgl so it's not trying to access the GPU for rendering
chrome_options.add_argument('--disable-webgl')
# Disable an infobar informing the browser that it's being controlled by automation software
chrome_options.add_argument("--disable-infobars")
# Overcome limited resource problems
chrome_options.add_argument("--disable-dev-shm-usage")
# Set a custom user agent string that mimics a normal desktop user 
# (it's telling the browser the user uses Mozilla on windows 10 with a speciic webKit and KHTML engine, Chrome ver.91, and a ver. of Webkit to render for Safari)
chrome_options.add_argument(user_agent_string)


service = Service(PATH)

driver = webdriver.Chrome(service = service, options=chrome_options)
# Sends a Chrome DevTools Protocol (CDP) command to override the user-agent string
driver.execute_cdp_cmd('Network.setUserAgentOverride', {"userAgent": user_agent_string_override_command})


driver.get(samsung_odyssey_g5_ceneo_url)
samsung_odyssey_g5_ceneo_prices = scrape_ceneo_price(driver=driver)



df = pd.read_csv("samsung_g5_price_history.csv", header=0, index_col=0)
df['data'] = pd.to_datetime(df['data'])




current_price = samsung_odyssey_g5_ceneo_prices[0]
formatted_time = pd.to_datetime(datetime.now())

print(f'\n cena: {current_price}, data: {formatted_time}')

df.loc[len(df)] = [current_price, formatted_time]
    
df.to_csv('samsung_g5_price_history.csv')    
print('\ndodano wiersz do historii')
