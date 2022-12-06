from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service = Service('../../chrome webdriver/chromedriver.exe')

driver = webdriver.Chrome(service=service)
driver.get("https://www.amazon.in/New-Apple-iPhone-11-64GB/dp/B08L89J9G3/ref=sr_1_1_sspa?crid=3VAQZV4OGQ7VR&keywords=iphone&qid=1662132098&sprefix=%2Caps%2C177&sr=8-1-spons&psc=1")

price = driver.find_element(By.CSS_SELECTOR, "span .a-price-whole")
price = (price.get_attribute("innerHTML")).split("<")[0].split(",")
price = f"{price[0]}{price[1]}"
print(price)

name = driver.find_element(By.ID, "productTitle")
name = name.text
print(name)

pricer = driver.find_element(By.XPATH, '//*[@id="corePriceDisplay_desktop_feature_div"]/div[1]/span[2]/span[1]')
print(pricer.get_attribute("innerHTML"))
driver.quit()

