import smtplib
my_email = "pratiktest610@gmail.com"
password = "hbeetpiottmakqzc"

class MailManager:

    def __init__(self):
        pass

    def send_email(self, msg , email):
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(my_email, password)
            connection.sendmail(my_email, email, msg)
