import numpy as np
import pandas as pd
import requests
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time
from datetime import datetime
import matplotlib.pyplot as plt
import seaborn as sns
from bs4 import BeautifulSoup

price_df = pd.DataFrame(columns=['price', 'time'])

while True:
    PATH  = './chromedriver-win64/chromedriver.exe'

    samsung_monitor_morele_url = 'https://www.morele.net/monitor-samsung-viewfinity-s50gc-ls34c500gauxen-12767113/?utm_source=google&utm_medium=cpc&utm_campaign=20541966716&gad_source=1&gclid=Cj0KCQjwurS3BhCGARIsADdUH52flXIPpOT1haDmjaqYwsxML8CLmVd_urm1PDxjgiPR1H1GmQytKT0aAnkDEALw_wcB'

    service = Service(PATH)

    driver = webdriver.Chrome(service = service)
    driver.get(samsung_monitor_morele_url)

    time.sleep(3)#to let the webiste load

    html = driver.page_source

    soup = BeautifulSoup(html, 'html.parser')

    product_prices = soup.find_all('div', class_='product-price')

    price = product_prices[0].text.strip()
    formatted_price = float(price.replace('zł', '').replace(' ', '').replace(',', '.'))
    t = datetime.now()
    formatted_time = t.strftime("%d/%m/%Y %H:%M:%S")
            
    driver.quit()

    print(f'cena: {formatted_price}, data: {formatted_time}')

    with open('price_history.csv', 'a', encoding='utf-8') as file:
        file.write(f'{i},{formatted_price},{formatted_time}\n')
        file.close()
        
    print('dodano wiersz do historii')
    
    time.sleep(3600)
        

"""# Tworzenie pustego wykresu
x, y = [], []
plt.ion()  # Tryb interaktywny

fig, ax = plt.subplots()
line, = ax.plot(x, y)

# Aktualizacja danych w czasie rzeczywistym
for i in range(100):
    x.append(i)
    y.append(np.sin(i / 10.0))
    
    line.set_xdata(x)
    line.set_ydata(y)
    ax.relim()  # Przeliczenie granic
    ax.autoscale_view()
    
    #plt.draw()
    plt.pause(0.1)  # Pauza, aby można było zobaczyć aktualizacje
    time.sleep(0.1)

plt.ioff()  # Wyłączanie trybu interaktywnego
plt.show()"""