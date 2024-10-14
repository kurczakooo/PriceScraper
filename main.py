import numpy as np
import pandas as pd
import requests
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time
from datetime import datetime
import matplotlib.pyplot as plt
import seaborn as sns
from bs4 import BeautifulSoup

price_df = pd.DataFrame(columns=['price', 'time'])


PATH  = './chromedriver-win64/chromedriver.exe'

PATH_LINUX = '/usr/bin/chromedriver/chromedriver'

samsung_monitor_morele_url = 'https://www.morele.net/monitor-samsung-viewfinity-s50gc-ls34c500gauxen-12767113/?utm_source=google&utm_medium=cpc&utm_campaign=20541966716&gad_source=1&gclid=Cj0KCQjwurS3BhCGARIsADdUH52flXIPpOT1haDmjaqYwsxML8CLmVd_urm1PDxjgiPR1H1GmQytKT0aAnkDEALw_wcB'

chrome_options = Options()
chrome_options.add_argument("--headless")  # Tryb bezokienkowy
chrome_options.add_argument("--no-sandbox")  # Disable sandbox for headless mode
chrome_options.add_argument("--disable-dev-shm-usage")  # Overcome limited resource problems

service = Service(PATH_LINUX)

current_price = 0

driver = webdriver.Chrome(service = service, options=chrome_options)

driver.get(samsung_monitor_morele_url)
time.sleep(3)#to let the webiste load

html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')
product_prices = soup.find_all('div', class_='product-price')
driver.quit()

price = product_prices[0].text.strip()
current_price = price
formatted_price = float(price.replace('zł', '').replace(' ', '').replace(',', '.'))
t = datetime.now()
formatted_time = t.strftime("%d/%m/%Y %H:%M:%S")

print(f'cena: {formatted_price}, data: {formatted_time}')

with open('price_history.csv', 'a', encoding='utf-8') as file:
    file.write(f'{2},{formatted_price},{formatted_time}\n')
    file.close()
    
print('dodano wiersz do historii')
