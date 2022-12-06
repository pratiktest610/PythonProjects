from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.common.exceptions import ElementClickInterceptedException
import time

instagram = "https://www.instagram.com/accounts/login/"
my_email = "pratiktest610@gmail.com"
my_password = "4453040pl"
target = "nike"

service = Service("C:/Users/geeta/chrome webdriver/chromedriver.exe")

class InstagramFollowBot:
    def __init__(self):
        self.driver = webdriver.Chrome(service=service)

    def login(self):
        self.driver.get(instagram)

        time.sleep(5)
        username = self.driver.find_element(By.XPATH, '//input[@name="username"]')
        password = self.driver.find_element(By.XPATH, '//input[@name="password"]')

        username.send_keys(my_email)
        password.send_keys(my_password)
        password.send_keys(Keys.ENTER)

    def find_followers(self):

        time.sleep(5)
        search = self.driver.find_element(By.XPATH, '//input[@placeholder="Search"]')
        search.send_keys(target)
        time.sleep(1)
        search.send_keys(Keys.ENTER)
        search.send_keys(Keys.ENTER)

        time.sleep(5)
        followers = self.driver.find_element(By.XPATH, '//a[@role="link"]')
        followers.click()
        time.sleep(3)

    def follow(self, times=1):
        for i in range(times):
            buttons = self.driver.find_elements(By.XPATH, '//button[@class="_acan _acap _acas"]')
            print(len(buttons))

            for button in buttons:
                time.sleep(3)
                self.driver.execute_script("arguments[0].click();", button)


bot = InstagramFollowBot()
bot.login()
bot.find_followers()
bot.follow(10)

