from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
import time

my_username = "pratiktest610@gmail.com"
my_password = "4453040pl"
prom_up_speed = 100
prom_down_speed = 40
service = Service("C:/Users/geeta/chrome webdriver/chromedriver.exe")

speed_test_url = "https://www.speedtest.net/"
twitter_url = "https://twitter.com/i/flow/login"

class SpeedTestTwitterBot:
    def __init__(self):
        self.driver = webdriver.Chrome(service=service)
        self.up_speed = None
        self.down_speed = None

    def get_internet_speed(self):
        self.driver.get(speed_test_url)
        go = self.driver.find_element(By.XPATH, '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[1]/a/span[4]')
        go.click()
        time.sleep(60)
        print("times up")
        self.up_speed = self.driver.find_element(By.XPATH, '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span').text
        self.down_speed = self.driver.find_element(By.XPATH, '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[1]/div/div[2]/span').text
        print(self.down_speed, self.up_speed)

    def tweet_to_provider(self, msg):
        self.driver.get(twitter_url)

        time.sleep(5)
        username = self.driver.find_element(By.XPATH, '//input[@autocomplete="username"]')
        username.send_keys(my_username)
        time.sleep(2)
        username.send_keys(Keys.ENTER)

        try:
            time.sleep(2)
            password = self.driver.find_element(By.XPATH, '//input[@name="password"]')
            password.send_keys(my_password)
            time.sleep(2)
            password.send_keys(Keys.ENTER)
        except NoSuchElementException:
            phone = self.driver.find_element(By.XPATH, '//input[@name="text"]')
            phone.send_keys('8169321278')
            time.sleep(2)
            phone.send_keys(Keys.ENTER)

            time.sleep(2)
            password = self.driver.find_element(By.XPATH, '//input[@name="password"]')
            password.send_keys(my_password)
            time.sleep(2)
            password.send_keys(Keys.ENTER)

        time.sleep(5)
        text = self.driver.find_element(By.XPATH, "//div[contains(@aria-label, 'Tweet text')]")
        text.send_keys(msg)
        time.sleep(2)
        tweet_button = self.driver.find_element(By.XPATH, '//div[@data-testid="tweetButtonInline"]')
        self.driver.execute_script("arguments[0].click();", tweet_button)


bot = SpeedTestTwitterBot()
bot.get_internet_speed()

if float(bot.down_speed) < prom_down_speed or float(bot.up_speed) < prom_up_speed:
    msg = f"Hey, Internet Provider, my internet speed is {bot.down_speed}down/{bot.up_speed}up," \
          f" when I pay for for a 100mb plan. why?"
    bot.tweet_to_provider(msg)
