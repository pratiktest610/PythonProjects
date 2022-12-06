from urllib import request
from flask import Flask, render_template
import random
import datetime as dt
import requests

app = Flask(__name__)


@app.route("/")
def home():
    random_number = random.randint(0, 10)
    current_year = dt.datetime.now().year
    return render_template("index.html", num=random_number, year=current_year)

@app.route("/guess/<name>")
def guess_user_info(name):
    parameter = {"name": name}

    response1 = requests.get(url="https://api.agify.io", params=parameter)
    age = response1.json()["age"]

    response1 = requests.get(url="https://api.genderize.io", params=parameter)
    gender = response1.json()["gender"]

    return render_template("guess.html", name=name, age=age, gender=gender)

@app.route("/blog/<num>")
def get_blog(num):
    blogs_url = "https://api.npoint.io/c790b4d5cab58020d391"
    response = requests.get(url=blogs_url)
    blogs = response.json()
    return render_template("blog.html", blogs=blogs)

if __name__ == "__main__":
    app.run(debug=True) 


