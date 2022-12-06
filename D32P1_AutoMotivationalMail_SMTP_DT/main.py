import datetime as dt
import smtplib
import random

now = dt.datetime.now()
week_day = now.weekday()

with open("quotes.txt") as file:
    quotes_list = file.readlines()

my_email = "pratiktest610@gmail.com"
password = "hbeetpiottmakqzc"
to_email = "pratiktest610@yahoo.com"
message = f"Subject:Weekly Motivation\n\n{random.choice(quotes_list)}"

if week_day == 1:
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email, to_addrs=to_email, msg=message)
