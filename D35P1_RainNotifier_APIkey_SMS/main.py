import requests
import smtplib

my_lat = 21
my_long = 79

api_key = "69f04e4613056b159c2761a9d9e664d2"
api_endpoint ="https://api.openweathermap.org/data/2.5/onecall"

my_email = "pratiktest610@gmail.com"
password = "hbeetpiottmakqzc"
to_email = "pratiktest610@yahoo.com"
message = "Subject:Carry your umbrella.\n\nIt's gonna rain today!!"

weather_data = None


def get_weather_data():
    global weather_data
    parameters = {
        "lat": my_lat,
        "lon": my_long,
        "appid": api_key,
        "exclude": "current,minutely,daily"
    }
    response = requests.get(url=api_endpoint, params=parameters)
    response.raise_for_status()
    weather_data = response.json()


def send_email():
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(my_email, password)
        connection.sendmail(my_email, to_email, message )


def its_raining():
    for hour in range(12):
        code = weather_data["hourly"][hour]["weather"][0]["id"]
        if code < 700:
            return True


get_weather_data()
if its_raining():
    send_email()
    print("email sent!!")
