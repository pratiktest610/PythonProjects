import requests
from bs4 import BeautifulSoup
import smtplib
budget = 42000
product_url = "https://www.flipkart.com/apple-iphone-11-white-64-gb/p/itmfc6a7091eb20b?pid=MOBFWQ6BVWVEH3XE&lid=LSTMOBFWQ6BVWVEH3XEMXQMLO&marketplace=FLIPKART&q=iphone&store=tyy%2F4io&srno=s_1_1&otracker=search&otracker1=search&fm=organic&iid=fc99c29f-3ef2-4816-9c24-cffff3d917c1.MOBFWQ6BVWVEH3XE.SEARCH&ppt=hp&ppn=homepage&ssid=rhbzu34b280000001662110808054&qH=0b3f45b266a97d70"

response = requests.get(product_url)
webpage = response.text

soup = BeautifulSoup(webpage, "html.parser")

product_name = soup.find(name="span", class_="B_NuCI").getText()

price = soup.find(name="div", class_="_30jeq3 _16Jk6d").getText()
price = price.split("₹")[1].split(",")
price = int(f"{price[0]}{price[1]}")

my_email = "pratiktest610@gmail.com"
password = "hbeetpiottmakqzc"
to_email = "pratiktest610@yahoo.com"
message = f"Subject:Price Drop Alert!!\n\n{product_name} is available @ only{price}.\n Buy Now @ {product_url}"

if price < budget:
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(my_email, password)
        connection.sendmail(my_email, to_email, message)
