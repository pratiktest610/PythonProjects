from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.chrome.service import Service
import time

linkedin_url = "https://www.linkedin.com/jobs/search/?currentJobId=3245731207&f_AL=true&keywords=python%20programmer&refresh=true&sortBy=R"
my_email = "pratiktest610@gmail.com"
my_password = "4453040pl"

service = Service("C:/Users/geeta/chrome webdriver/chromedriver.exe")
driver = webdriver.Chrome(service=service)

driver.get(linkedin_url)
signin = driver.find_element(By.XPATH, "/html/body/div[1]/header/nav/div/a[2]")
signin.click()

username = driver.find_element(By.ID, "username")
username.send_keys(my_email)

password = driver.find_element(By.ID, "password")
password.send_keys(my_password)
password.send_keys(Keys.ENTER)

# time.sleep(10)
# apply_job = driver.find_element(By.XPATH, '//*[@id="ember331"]')
# apply_job.click()
#
# phone = driver.find_element(By.XPATH, '//*[@id="urn:li:fs_easyApplyFormElement:(urn:li:fs_normalized_jobPosting:3245731207,67812749,phoneNumber~nationalNumber)"]')
# time.sleep(2)
# phone.send_keys("9452639875")
#
# nextbutton = driver.find_element(By.XPATH, '//*[@id="ember349"]')
# nextbutton.click()

save = driver.find_element(By.XPATH, '//*[@id="main"]/div/section[2]/div/div[2]/div[1]/div/div[1]/div/div[1]/div[1]/div[3]/div/button')

jobs = driver.find_elements(By.CLASS_NAME, "jobs-search-results__list-item")
print(len(jobs))
for job in jobs:
    time.sleep(1)
    job.click()
    time.sleep(2)
    save.click()




