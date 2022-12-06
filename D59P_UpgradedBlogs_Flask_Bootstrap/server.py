from flask import Flask, render_template, request
import requests
import smtplib

my_email = "pratiktest610@gmail.com"
password = "hbeetpiottmakqzc"
to_email = "pratiktest610@yahoo.com"

data_url = "https://api.npoint.io/5deaf41b4f8078c817e6"
response = requests.get(data_url)
data = response.json()

def send_email(name, email, phone, msg):
    message = f"Subject:Message From Website Visitor\n\nName: {name}\nEmail: {email}\nPhone: {phone}\nMessage: {msg}"
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email, to_addrs=to_email, msg=message)


app = Flask(__name__)

@app.route("/")
def homepage():
    return render_template("index.html", data=data)

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/post/<id>")
def get_post(id):
    index = int(id) - 1
    return render_template("post.html", data=data, index=index)

@app.route("/contact", methods=["POST", "GET"])
def contact():
    if request.method == "POST":
        data = request.form
        name = (data["name"])
        email = (data["email"])
        phone = (data["phone"])
        message = (data["message"])
        send_email(name, email, phone, message)
        msg = "Successfully Sent Your Message"
        return render_template("contact.html", msg=msg)
    msg = "Contact Me"
    return render_template("contact.html", msg=msg)

if __name__ == "__main__":
    app.run(debug=True)

