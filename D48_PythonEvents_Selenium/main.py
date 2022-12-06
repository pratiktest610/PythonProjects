from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service = Service("C:/Users/geeta/chrome webdriver/chromedriver.exe")
driver = webdriver.Chrome(service=service)


driver.get("https://www.python.org/")
div = driver.find_element(By.XPATH, '//*[@id="content"]/div/section/div[2]/div[2]/div')
ulist = div.find_element(By.CLASS_NAME, "menu")
dates = ulist.find_elements(By.CSS_SELECTOR, "time")
names = ulist.find_elements(By.CSS_SELECTOR, "a")

event_calender = {}
for i in range(len(names)):
    event_calender[i] = {
        "Date": dates[i].text,
        "Name": names[i].text
    }
print(event_calender)
driver.quit()

