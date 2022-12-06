import requests
import datetime as dt
import smtplib

now = dt.datetime.utcnow()
newyork_now = now - dt.timedelta(hours=4)
newyork_today = newyork_now.date()
newyork_y = newyork_today - dt.timedelta(days=1)
newyork_dby = newyork_today - dt.timedelta(days=2)


COMPANY_NAME = "TESLA INC"
stock_symbol = "TSLA"

stock_api_key = "45Y2PQQ9F1M52GWV"
stock_url = "https://www.alphavantage.co/query"
stock_function = "TIME_SERIES_DAILY"

news_api_key = "8c5c2b05a7d94541b736bc1436d22b1f"
news_url = "https://newsapi.org/v2/everything"

my_email = "pratiktest610@gmail.com"
password = "hbeetpiottmakqzc"
to_email = "pratiktest610@yahoo.com"


def get_news(index):
    parameters = {
        "apiKey": news_api_key,
        "q": COMPANY_NAME,
        "from": newyork_dby,
        "to": newyork_y,
        "sortBy": "popularity"
     }
    response = requests.get(url=news_url, params=parameters)
    news_data = response.json()

    title = (news_data["articles"][index]["title"])
    info = (news_data["articles"][index]["description"])
    source = (news_data["articles"][index]["source"]["name"])

    news = f"Headline: {title}\n\nBrief: {info}\n\nSourse:{source}"

    return news


def get_stock_data():

    parameters = {
        "function": stock_function,
        "symbol": stock_symbol,
        "apikey": stock_api_key,
    }
    response = requests.get(url=stock_url, params=parameters)
    response.raise_for_status()
    stock_data = response.json()

    dby_close = float(stock_data["Time Series (Daily)"][str(newyork_dby)]["4. close"])
    y_close = float(stock_data["Time Series (Daily)"][str(newyork_y)]["4. close"])
    dif_cent = round(((y_close - dby_close) / dby_close) * 100, 2)

    return dif_cent


def send_email(sub):
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(my_email, password)
        for index in range(3):
            message = get_news(index)
            message = message.encode('ascii', 'ignore').decode('ascii')
            connection.sendmail(my_email, to_email, msg=f"Subject:{sub}\n\n{message}")
            print("mail sent")


diff_cent = get_stock_data()
print(diff_cent)

if diff_cent < 0:
    subject = f"{COMPANY_NAME} stocks down by {-1 * diff_cent}% !!"
    send_email(subject)


if diff_cent > 0:
    subject = f"{COMPANY_NAME} stocks up by {diff_cent}%!!"
    send_email(subject)



