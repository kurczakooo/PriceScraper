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
from allegro_through_ceneo.captcha_allegro import do_captcha

price_df = pd.DataFrame(columns=['price', 'time'])


PATH  = './chromedriver-win64/chromedriver.exe'

PATH_LINUX = '/usr/bin/chromedriver/chromedriver'


chrome_options = Options()
#chrome_options.add_argument("--headless")  # Tryb bezokienkowy
#chrome_options.add_argument("--no-sandbox")  # Disable sandbox for headless mode
#chrome_options.add_argument("--disable-dev-shm-usage")  # Overcome limited resource problems

service = Service(PATH)

current_price = 0
price = ""

driver = webdriver.Chrome(service = service, options=chrome_options)

driver.get(samsung_odyssey_g5_allegro_url)

# time.sleep(100)

try:
    WebDriverWait(driver, 50).until(
        EC.presence_of_element_located((By.CLASS_NAME, 'cookie-consent__buttons__action js_cookie-consent-agree primary'))    
    )
    button = driver.find_element(By.CLASS_NAME, 'cookie-consent__buttons__action js_cookie-consent-agree primary')
    button.click()
    
    WebDriverWait(driver, 50).until(
        EC.presence_of_element_located((By.CLASS_NAME, 'price'))    
    )
    html = driver.page_source
    soup = BeautifulSoup(html, 'html.parser')
    product_prices = soup.find_all('div', class_='price')
    print(product_prices)
    #price = product_prices[0].text.strip()
     
except Exception as e:
    print(f'Error: {e}')
finally:
    driver.quit()

# current_price = price
# formatted_price = float(price.replace('zł', '').replace(' ', '').replace(',', '.'))
# t = datetime.now()
# formatted_time = t.strftime("%d/%m/%Y %H:%M:%S")

# print(f'cena: {formatted_price}, data: {formatted_time}')

# with open('price_history.csv', 'a', encoding='utf-8') as file:
#     file.write(f'{2},{formatted_price},{formatted_time}\n')
#     file.close()
    
# print('dodano wiersz do historii')
