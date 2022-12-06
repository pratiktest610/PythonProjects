from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service

service = Service("C:/Users/geeta/chrome webdriver/chromedriver.exe")
driver = webdriver.Chrome(service=service)

driver.get("http://secure-retreat-92358.herokuapp.com/")
fname_box = driver.find_element(By.XPATH, '/html/body/form/input[1]')
lname_box = driver.find_element(By.XPATH, '/html/body/form/input[2]')
email_box = driver.find_element(By.XPATH, '/html/body/form/input[3]')

fname_box.send_keys("Pratik")
lname_box.send_keys("Yadav")
email_box.send_keys("Pratik@email.com")
email_box.send_keys(Keys.ENTER)

driver.quit()