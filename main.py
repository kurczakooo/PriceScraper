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

print(prices[0])

# current_price = price
# formatted_price = float(price.replace('zł', '').replace(' ', '').replace(',', '.'))
# t = datetime.now()
# formatted_time = t.strftime("%d/%m/%Y %H:%M:%S")

# print(f'cena: {formatted_price}, data: {formatted_time}')

# with open('price_history.csv', 'a', encoding='utf-8') as file:
#     file.write(f'{2},{formatted_price},{formatted_time}\n')
#     file.close()
    
# print('dodano wiersz do historii')
