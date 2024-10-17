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
from urls import samsung_odyssey_g5_allegro_url
from ceneo.scrape_price import scrape_ceneo_price

price_df = pd.DataFrame(columns=['price', 'time'])


PATH  = './chromedriver-win64/chromedriver.exe'

PATH_LINUX = '/usr/bin/chromedriver/chromedriver'


chrome_options = Options()
#chrome_options.add_argument("--headless")  # Tryb bezokienkowy
#chrome_options.add_argument("--no-sandbox")  # Disable sandbox for headless mode
#chrome_options.add_argument("--disable-dev-shm-usage")  # Overcome limited resource problems

service = Service(PATH)

driver = webdriver.Chrome(service = service, options=chrome_options)

driver.get(samsung_odyssey_g5_allegro_url)

prices = scrape_ceneo_price(driver=driver)



df = pd.read_csv("samsung_g5_price_history.csv", header=0, index_col=0)
df['data'] = pd.to_datetime(df['data'])




current_price = prices[0]
formatted_time = pd.to_datetime(datetime.now())

print(f'cena: {current_price}, data: {formatted_time}')

df.loc[len(df)] = [current_price, formatted_time]

print(df.dtypes)
    
    
df.to_csv('samsung_g5_price_history.csv')    
print('\ndodano wiersz do historii')
