""""python selenium program to work with Xpath and extraction of followers and followings
DATE:19-DEC-2-24"""
import time
from calendar import error

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from time import sleep
"""instagram credantials"""

import os

     username = os.getenv('IG_USERNAME')
     password = os.getenv('IG_PASSWORD')

""""profile to extract details"""

    profile_username= 'https://www.instagram.com/guviofficial/'

""'initiliaze webdriver"""

    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

""""login instagram"""

def login():
    driver.get("https://www.instagram.com/accounts/login/")
    sleep(4)

    """"username and password login"""
    driver.find_element(By.NAME, 'username').send_keys(username)
    driver.find_element(By.NAME,'password').send_keys(password)
    driver.find_element(By.NAME,'password').send_keys(keys.RETURN)
    sleep(4)


    def extract_counts():
        driver.get(profile_url)
        sleep(4)


        try:
            followers_xpath = "//a[contains(@href,'/guviofficial/followers/')and @role='link']//span[@title]"
            following_xpath = "//a[contains(@href,'/guviofficial/following/') and @role='link']"

            print(f"Followers:{followers_count}")
            print(f"Followings:{following_count}")
        except Exception as error:
            print("ERROR", error)

            def main()
                login()
                extract_counts()

                driver.quit()

                if __name__= "main":
                    main()
