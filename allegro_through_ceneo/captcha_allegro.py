from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def do_captcha(driver):
    try:
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, 'captcha_display_button_submit'))
        )
        button = driver.find_element(By.CLASS_NAME, 'captcha_display_button_submit')
        button.click()
    except Exception as e:
        print(f'Error in alegro captcha: {e}')