from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import datetime as dt

service = Service("C:/Users/geeta/chrome webdriver/chromedriver.exe")
driver = webdriver.Chrome(service=service)

driver.get("http://orteil.dashnet.org/experiments/cookie/")
cookie = driver.find_element(By.ID, "cookie")

play = True
start_time = dt.datetime.now()
i = 1
while play:
    items = driver.find_elements(By.CSS_SELECTOR, "#store div")
    items.reverse()
    cookie.click()
    if dt.datetime.now() >= start_time + dt.timedelta(seconds=(i * 5)):
        i += 1
        for item in items:
            if item.get_attribute("class") != "grayed":
                item.click()
                break
    if dt.datetime.now() > start_time + dt.timedelta(minutes=5):
        play = False


