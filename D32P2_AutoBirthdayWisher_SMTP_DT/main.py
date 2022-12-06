import datetime as dt
import pandas
import smtplib
import random

now = dt.datetime.now()
today = now.day
tomonth = now.month


def send_email(receivers_email, message_to_send):
    my_email = "pratiktest610@gmail.com"
    password = "hbeetpiottmakqzc"
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(my_email, password)
        connection.sendmail(my_email, receivers_email, f"Subject:HAPPY BIRTHDAY!\n\n{message_to_send}")


def create_message(birthday_person):
    birthday_message = ""
    format = random.choice(formats)
    for line in format:
        birthday_message += line
    birthday_message = birthday_message.replace("[NAME]", birthday_person)
    return birthday_message


with open("letter_templet/letter_1.txt") as file1:
    format_1 = file1.readlines()
with open("letter_templet/letter_2.txt") as file2:
    format_2 = file2.readlines()
with open("letter_templet/letter_3.txt") as file3:
    format_3 = file3.readlines()

formats = [format_3, format_2, format_1]

on = True
while on:
    days = []
    months = []
    try:
        data = pandas.read_csv("new_birthday.csv")
    except FileNotFoundError:
        data = pandas.read_csv("birthdays.csv")

    data_dict = data.to_dict(orient="index")
    for i in range(len(data)):
        month = data_dict[i]["month"]
        months.append(month)
        day = data_dict[i]["day"]
        days.append(day)

    if today in days and tomonth in months:
        index_day = days.index(today)
        index_month = months.index(tomonth)
        if index_day == index_month:

            index = index_day
            name = data_dict[index]["name"]
            to_email = data_dict[index]["email"]

            message = create_message(name)
            send_email(to_email, message)
            print(f"Mail send to {name}")

            data = data.drop(index)
            data = data.reset_index(drop=True)
            data.to_csv("new_birthday.csv")

        else:
            print("No more birthdays today")
            on = False
    else:
        print("No more birthdays today")
        on = False
