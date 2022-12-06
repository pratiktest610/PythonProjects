from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import datetime as dt
import time


service = Service("C:/Users/geeta/chrome webdriver/chromedriver.exe")
driver = webdriver.Chrome(service=service)

driver.get("http://orteil.dashnet.org/experiments/cookie/")
cookie = driver.find_element(By.ID, "cookie")

play = True
now = dt.datetime.now().second

while True:
    items = driver.find_elements(By.CSS_SELECTOR, "#store div")
    items.reverse()
    cookie.click()
    new_now = dt.datetime.now().second
    new_now_min = dt.datetime.now().min
    if new_now % 5 == 0 and now != new_now:
        now = new_now
        for item in items:
            if item.get_attribute("class") != "grayed":
                item.click()
                break



driver.quit()