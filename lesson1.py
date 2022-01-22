from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from auth_data import username, password
import time
import random

PATH = 'C:/Users/Макс/PycharmProjects/InstagramBot/chromedriver/chromedriver.exe'
INSTAGRAM = 'https://www.instagram.com'


def login(username, passsword):
    browser = webdriver.Chrome(PATH)

    try:
        browser.get(INSTAGRAM)
        time.sleep(random.randrange(3, 5))

        username_input = browser.find_element(By.NAME, 'username')
        username_input.clear()
        username_input.send_keys(username)

        time.sleep(2)

        password_input = browser.find_element(By.NAME, 'password')
        password_input.clear()
        password_input.send_keys(passsword)

        password_input.send_keys(Keys.ENTER)
        time.sleep(10)

        browser.close()
        browser.quit()
    except Exception as ex:
        print(ex)
        browser.close()
        browser.quit()


login(username, password)
