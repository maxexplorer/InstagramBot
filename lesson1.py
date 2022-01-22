from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from auth_data import username, password
import time
import random

PATH = 'C:/Users/Макс/PycharmProjects/InstagramBot/chromedriver/chromedriver.exe'
INSTAGRAM = 'https://www.instagram.com'


def hashtag_search(username, password, hashtag):
    hashtag_path = f'https://www.instagram.com/explore/tags/{hashtag}/'
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
        password_input.send_keys(password)

        password_input.send_keys(Keys.ENTER)
        time.sleep(5)

        try:
            browser.get(hashtag_path)
            time.sleep(5)
            hrefs = browser.find_elements(By.TAG_NAME, 'a')
            posts_urls = []
            for item in hrefs:
                href = item.get_attribute('href')
                if '/p/' in href:
                    posts_urls.append(href)
                    print(href)

        except Exception as ex:
            print(ex)

        browser.close()
        browser.quit()
    except Exception as ex:
        print(ex)
        browser.close()
        browser.quit()


login(username, password)
