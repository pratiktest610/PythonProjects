# import smtplib
#
# my_email = "pratiktest610@gmail.com"
# password = "hbeetpiottmakqzc"
# message = "Subject:Hello\n\nHello, this is an automated mail. "
#
# with smtplib.SMTP("smtp.gmail.com") as connection:
#     connection.starttls()
#     connection.login(user=my_email, password=password)
#     connection.sendmail(from_addr=my_email, to_addrs="pratiktest610@yahoo.com", msg=message)

import datetime as dt

now = dt.datetime.now()
year = now.year
month = now.month
day = now.day
# print(year, month)

dob = dt.datetime(year=year, month=10, day=6)
print(dob)
