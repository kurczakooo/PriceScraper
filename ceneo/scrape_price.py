from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import time

def scrape_ceneo_price(driver) -> list:
    # GETS A LIST F PRICES FROM THE CENEO WEBSITE, THE FIRST ONE IS THE CHEAPEST ALWAYS, AND THERES A COUPLE 
    # WHICH ARE FROM OTHER THINGS ON THE SITE AND THEY DONT MATCH THE PRODUCT  
    prices = []
    
    try:
        #decline_ceneo_cookies(driver)
        WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.CLASS_NAME, 'product-offer__product__price'))    
        )
        html = driver.page_source
        soup = BeautifulSoup(html, 'html.parser')
        product_prices = soup.find_all('span', class_='price')
        
        for price in product_prices:
            value = price.find('span', class_='value').text
            penny = price.find('span', class_='penny').text
            full_price = float((value+penny).replace(',', '.').replace(' ', ''))
            prices.append(full_price)

    except Exception as e:
        print(f'Scraping Error: {e}')
    finally:
        driver.quit()
        return prices
  
  
        
def decline_ceneo_cookies(driver):
    try:
        WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, '.cookie-consent__buttons__action.js_cookie-consent-necessary'))    
        )
        button = driver.find_element(By.CSS_SELECTOR, '..cookie-consent__buttons__action.js_cookie-consent-necessary')
        button.click()
    except Exception as e:
        print(f'Declinig cookies Error: {e}')


