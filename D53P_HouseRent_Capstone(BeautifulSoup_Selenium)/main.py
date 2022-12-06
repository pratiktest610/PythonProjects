from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import requests
import time

headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 11_1)"
                  " AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0.2"
                  " Safari/605.1.15",
    "Accept-Language": "en-US"
}
form_url = "https://forms.gle/UjfAzwd8Ef93SzGh9"
zillow_url = "https://www.zillow.com/homes/for_rent/?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C%22mapBounds%22%3A%7B%22west%22%3A-122.56825484228516%2C%22east%22%3A-122.29840315771484%2C%22south%22%3A37.69234177970015%2C%22north%22%3A37.858148163315015%7D%2C%22mapZoom%22%3A12%2C%22isMapVisible%22%3Atrue%2C%22filterState%22%3A%7B%22price%22%3A%7B%22max%22%3A608469%7D%2C%22beds%22%3A%7B%22min%22%3A1%7D%2C%22fore%22%3A%7B%22value%22%3Afalse%7D%2C%22mp%22%3A%7B%22max%22%3A2800%7D%2C%22auc%22%3A%7B%22value%22%3Afalse%7D%2C%22nc%22%3A%7B%22value%22%3Afalse%7D%2C%22fr%22%3A%7B%22value%22%3Atrue%7D%2C%22fsbo%22%3A%7B%22value%22%3Afalse%7D%2C%22cmsn%22%3A%7B%22value%22%3Afalse%7D%2C%22fsba%22%3A%7B%22value%22%3Afalse%7D%7D%2C%22isListVisible%22%3Atrue%7D"

# ----------------------------------------Scraping Site Using bs4---------------------------------------- #
response = requests.get(zillow_url, headers=headers)
webpage = response.text

soup = BeautifulSoup(webpage, "html.parser")

price_elements = soup.select("div .list-card-price")
prices = [price.text.split(" ")[0].split("/")[0] for price in price_elements]
print(prices)

address_elements = soup.select("div .list-card-addr")
address = [add.text for add in address_elements]
print(address)

link_elements = soup.select("div .list-card-info a ")
links = [link['href'] for link in link_elements]
print(links)

# ----------------------------------------Filling Form Using Selenium---------------------------------------- #

service = Service("C:/Users/geeta/chrome webdriver/chromedriver.exe")
driver = webdriver.Chrome(service=service)

driver.get(form_url)



for i in range(len(links)):
    price_form = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
    address_form = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
    link_form = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')
    submit = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div/span/span')

    price_form.send_keys(prices[i])
    time.sleep(2)
    address_form.send_keys(address[i])
    time.sleep(2)
    link_form.send_keys(links[1])
    time.sleep(2)
    submit.click()
    time.sleep(5)
    new = driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div[1]/div/div[4]/a')
    new.click()


time.sleep(100)
